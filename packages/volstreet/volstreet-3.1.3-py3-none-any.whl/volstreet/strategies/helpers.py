import numpy as np
from attrs import define, field, validators
from volstreet.config import logger
from volstreet.blackscholes import greeks, Greeks
from volstreet.utils.core import time_to_expiry
from volstreet.dealingroom import (
    Strangle,
    Straddle,
    Option,
    place_option_order_and_notify,
)


@define(slots=False)
class DeltaPositionMonitor:
    instrument: Straddle | Strangle | Option = field(
        validator=validators.instance_of((Straddle, Strangle, Option))
    )
    initial_position_info: dict
    _call_active_qty = field(validator=validators.instance_of(int))
    _put_active_qty = field(validator=validators.instance_of(int))
    _total_premium = field(validator=validators.instance_of(float))
    underlying_ltp: float = field(
        validator=validators.instance_of(float), repr=False, default=np.nan
    )
    call_ltp: float = field(
        validator=validators.instance_of(float), default=np.nan, repr=False
    )
    put_ltp: float = field(
        validator=validators.instance_of(float), default=np.nan, repr=False
    )
    call_greeks: Greeks = field(init=False, repr=False)
    put_greeks: Greeks = field(init=False, repr=False)
    positional_greeks: Greeks = field(init=False, repr=False)
    delta_threshold: float = field(validator=validators.instance_of(float), init=False)
    exit_triggers: dict[str, bool] = field(
        factory=lambda: {"end_time": False, "qty_breach": False}
    )

    @_call_active_qty.default
    def _call_active_qty_default(self):
        return self.initial_position_info["Initial Qty"] * -1

    @_put_active_qty.default
    def _put_active_qty_default(self):
        return self.initial_position_info["Initial Qty"] * -1

    @_total_premium.default
    def _total_premium_default(self):
        return (
            self.initial_position_info["Initial Qty"]
            * self.initial_position_info["Total Entry Price"]
        )

    @property
    def call_active_qty(self):
        return self._call_active_qty

    @call_active_qty.setter
    def call_active_qty(self, value):
        if value > self._call_active_qty:
            raise ValueError("Call active short qty should only increase.")
        self._call_active_qty = value

    @property
    def put_active_qty(self):
        return self._put_active_qty

    @put_active_qty.setter
    def put_active_qty(self, value):
        if value > self._put_active_qty:
            raise ValueError("Put active short qty should only increase.")
        self._put_active_qty = value

    @property
    def total_premium(self):
        return self._total_premium

    @total_premium.setter
    def total_premium(self, value):
        if value < self._total_premium:
            raise ValueError("Total premium should only increase.")
        self._total_premium = value

    def update_call_position(self, additional_qty: int, avg_price: float):
        self.call_active_qty -= additional_qty
        self.total_premium += additional_qty * avg_price

    def update_put_position(self, additional_qty: int, avg_price: float):
        self.put_active_qty -= additional_qty
        self.total_premium += additional_qty * avg_price

    def record_position_status(self):
        """Designed to periodically save the position status to a file."""
        pass


def calculate_option_greeks(
    last_traded_prices: tuple[float, float, float],
    instrument: Straddle,
) -> tuple[Greeks, Greeks]:
    # Time to expiry
    tte = time_to_expiry(instrument.expiry)

    underlying_ltp, call_ltp, put_ltp = last_traded_prices

    call_iv, put_iv, _ = instrument.fetch_ivs(
        spot=underlying_ltp, prices=(call_ltp, put_ltp)
    )
    call_iv = np.nan if call_iv is None else call_iv
    put_iv = np.nan if put_iv is None else put_iv
    call_greeks = greeks(
        S=underlying_ltp,
        K=instrument.strike,
        t=tte,
        r=0.06,
        sigma=call_iv,
        flag="c",
    )
    put_greeks = greeks(
        S=underlying_ltp,
        K=instrument.strike,
        t=tte,
        r=0.06,
        sigma=put_iv,
        flag="p",
    )

    return call_greeks, put_greeks


def calculate_position_greeks(
    last_traded_prices: tuple[float, float, float],
    position_monitor: DeltaPositionMonitor,
    instrument: Straddle,
) -> tuple[Greeks, Greeks, Greeks]:
    call_greeks, put_greeks = calculate_option_greeks(last_traded_prices, instrument)
    call_position_greeks: Greeks = call_greeks * position_monitor.call_active_qty
    put_position_greeks: Greeks = put_greeks * position_monitor.put_active_qty
    positional_greeks: Greeks = call_position_greeks + put_position_greeks
    return call_greeks, put_greeks, positional_greeks


def recommend_delta_action(
    straddle: Straddle,
    position_monitor: DeltaPositionMonitor,
    max_qty_shares: int,
) -> tuple[Straddle, int, bool] | tuple[None, None, bool]:
    position_delta = position_monitor.positional_greeks.delta

    if (
        position_delta >= position_monitor.delta_threshold
    ):  # Net delta is positive, sell the required qty of calls
        qty_to_sell = int(
            (abs(position_delta) - 0) / abs(position_monitor.call_greeks.delta)
        )
        instrument_to_sell = straddle.call_option
        breach = abs(position_monitor.call_active_qty) + qty_to_sell > max_qty_shares
    elif (
        position_delta <= -position_monitor.delta_threshold
    ):  # Net delta is negative, sell the required qty of puts
        qty_to_sell = int(
            (abs(position_delta) - 0) / abs(position_monitor.put_greeks.delta)
        )
        instrument_to_sell = straddle.put_option
        breach = abs(position_monitor.put_active_qty) + qty_to_sell > max_qty_shares
    else:
        return None, None, False

    # Rounding the qty to sell to the nearest lot size and calculating the number of lots
    qty_to_sell = int(qty_to_sell / instrument_to_sell.lot_size)

    return (
        (None, None, False)
        if qty_to_sell == 0
        else (instrument_to_sell, qty_to_sell, breach)
    )


def neutralize_delta(
    instrument_to_sell: Option,
    adj_qty_lots: int,
    position_monitor: DeltaPositionMonitor,
    strategy_tag: str,
    notifier_url: str,
) -> None:
    avg_price = place_option_order_and_notify(
        instrument_to_sell,
        "SELL",
        adj_qty_lots,
        "LIMIT",
        strategy_tag,
        notifier_url,
    )

    qty_in_shares = adj_qty_lots * instrument_to_sell.lot_size

    if instrument_to_sell.option_type.lower().startswith("c"):
        position_monitor.update_call_position(qty_in_shares, avg_price)
    elif instrument_to_sell.option_type.lower().startswith("p"):
        position_monitor.update_put_position(qty_in_shares, avg_price)
    else:
        raise ValueError("Invalid option type")
    logger.info(
        f"Delta neutralized by selling {adj_qty_lots} lots of {instrument_to_sell}"
    )
