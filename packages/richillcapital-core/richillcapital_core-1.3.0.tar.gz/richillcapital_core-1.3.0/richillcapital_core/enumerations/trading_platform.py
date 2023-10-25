

from ..abstractions import Enumeration


class TradingPlatform(Enumeration["TradingPlatform"]):
    MAX_LENGTH = 32
    
    XQ: "TradingPlatform"
    MultiCharts: "TradingPlatform"
    MultiChartsNet: "TradingPlatform"
    TradeStation: "TradingPlatform"
    TradingView: "TradingPlatform"
    CTrader: "TradingPlatform"
    MetaTrader: "TradingPlatform"
    NinjaTrader: "TradingPlatform"
    Quantower: "TradingPlatform"
    QuantConnect: "TradingPlatform"
    WealthLab: "TradingPlatform"

    def __init__(self, name: str, value: int) -> None:
        super().__init__(name, value)


XQ = TradingPlatform("XQ", 0)
MultiCharts = TradingPlatform("MultiCharts", 1)
MultiChartsNet = TradingPlatform("MultiCharts.Net", 2)
TradeStation = TradingPlatform("TradeStation", 3)
TradingView = TradingPlatform("TradingView", 4)
CTrader = TradingPlatform("CTrader", 5)
MetaTrader = TradingPlatform("MetaTrader", 6)
NinjaTrader = TradingPlatform("NinjaTrader", 7)
Quantower = TradingPlatform("Quantower", 8)
QuantConnect = TradingPlatform("QuantConnect", 9)
WealthLab = TradingPlatform("XQ", 10)