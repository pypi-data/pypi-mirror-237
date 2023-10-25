from assertpy import assert_that
from richillcapital_core.enumerations import TradingPlatform


class TestTradingPlatform:

    def test1(self) -> None:
        platform = TradingPlatform.from_name("XQ")

        assert_that(platform.value).is_equal_to(0)

    def test2(self) -> None:
        platform = TradingPlatform.from_name("TradingView")
        platform2 = TradingPlatform.from_value(4)

        assert_that(platform).is_same_as(platform2)

