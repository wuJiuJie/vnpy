"""
Defines constants and objects used in CtaStrategy App.
"""

from dataclasses import dataclass
from enum import Enum

from vnpy.trader.constant import Direction, Offset

APP_NAME = "CtaStrategy"
STOPORDER_PREFIX = "STOP"


class CtaOrderType(Enum):
    BUY = "买开"
    SELL = "卖平"
    SHORT = "卖开"
    COVER = "买平"


class StopOrderStatus(Enum):
    WAITING = "等待中"
    CANCELLED = "已撤销"
    TRIGGERED = "已触发"


class EngineType(Enum):
    LIVE = "实盘"
    BACKTESTING = "回测"


class BacktestingMode(Enum):
    BAR = 1
    TICK = 2


@dataclass
class StopOrder:
    vt_symbol: str
    order_type: CtaOrderType
    price: float
    volume: float
    stop_orderid: str
    strategy_name: str
    status: StopOrderStatus = StopOrderStatus.WAITING
    vt_orderid: str = ""

    def __post_init__(self):
        """"""
        self.direction, self.offset = ORDER_CTA2VT[self.order_type]


EVENT_CTA_LOG = "eCtaLog"
EVENT_CTA_STRATEGY = "eCtaStrategy"
EVENT_CTA_STOPORDER = "eCtaStopOrder"

ORDER_CTA2VT = {
    CtaOrderType.BUY: (Direction.LONG, Offset.OPEN),
    CtaOrderType.SELL: (Direction.SHORT, Offset.CLOSE),
    CtaOrderType.SHORT: (Direction.SHORT, Offset.OPEN),
    CtaOrderType.COVER: (Direction.LONG, Offset.CLOSE),
}
