from stock import Stock
from utilities.period import Period

class Estimator:
    annuallyInterestRate = 0.04
    periodForHistoricalPrices = Period.M6

    def __init__(self, stock: Stock) -> None:
        self.stock = stock