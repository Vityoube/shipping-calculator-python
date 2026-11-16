import os
from typing import Final
from dotenv import load_dotenv
from decimal import Decimal
from _decimal import ROUND_05UP, ROUND_UP, ROUND_DOWN, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_DOWN

class CalculatorConfig:
    rateScale: Final[int]
    roundingMode: Final[str]
    rateRanges: dict[Decimal, Decimal]

    RANGE_PREFIX: Final = "range."
    PRECISION_KEY: Final = "precision"
    ROUNDING_MODE_KEY: Final = "roundingMode"

    @staticmethod
    def loadConfig():
        load_dotenv()
        if (os.getenv(CalculatorConfig.PRECISION_KEY) is None):
            raise Exception("Precision not set")
        rateScale: int = int(os.getenv(CalculatorConfig.PRECISION_KEY))
        if (os.getenv(CalculatorConfig.ROUNDING_MODE_KEY) is None):
            raise Exception("roundingMode not set")
        roundingMode = (os.getenv(CalculatorConfig.ROUNDING_MODE_KEY)).upper()
        rateRanges: dict[Decimal, Decimal] = {}
        for [key, value] in os.environ.items():
            if key.startswith(CalculatorConfig.RANGE_PREFIX.upper()):
                rateRanges[Decimal(key.replace(CalculatorConfig.RANGE_PREFIX.upper(), "", 1))] = Decimal(value)
        if not rateRanges:
            raise Exception("rateRanges not set")
        return CalculatorConfig(
            rateScale=rateScale,
            roundingMode=roundingMode,
            rateRanges=rateRanges
        )


    def __init__(self, rateScale: Final[int], roundingMode: Final[str], rateRanges: Final[dict[Decimal, Decimal]]) -> None:
        self.rateScale = rateScale
        self.roundingMode = roundingMode
        self.rateRanges = rateRanges


