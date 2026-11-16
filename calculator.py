from decimal import Decimal, getcontext

from calculator_config import CalculatorConfig


class Calculator:

    def __init__(self):
        self.calculatorConfig = CalculatorConfig.loadConfig()
        getcontext().prec = self.calculatorConfig.rateScale
        getcontext().rounding = self.calculatorConfig.roundingMode

    def calculate(self, totalWeight: Decimal) -> Decimal:
        rate = self.findRate(totalWeight)
        return rate * totalWeight

    def findRate(self, totalWeight: Decimal) -> Decimal:
        nearestRange = None
        for [range, rate] in self.calculatorConfig.rateRanges.items():
            if totalWeight >= rate:
                if nearestRange is None or totalWeight - range < totalWeight - nearestRange:
                    nearestRange = range
        if nearestRange is None:
            raise Exception(f"Could not find a suitable rate for {totalWeight}")
        return self.calculatorConfig.rateRanges[nearestRange]