import sys

from calculator import Calculator
from decimal import Decimal


def main () -> None:
    calculator = Calculator()
    print(calculator.calculate(Decimal("9.56")))

if __name__ == "__main__":
    main()