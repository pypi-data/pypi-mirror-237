from optionsPricingAndGreeks.stock import Stock
from optionsPricingAndGreeks.utilities.period import Period

class Estimator:
    annuallyInterestRate = 0.04
    periodForHistoricalPrices = Period.M6

    def __init__(self, stock: Stock) -> None:
        self.stock = stock