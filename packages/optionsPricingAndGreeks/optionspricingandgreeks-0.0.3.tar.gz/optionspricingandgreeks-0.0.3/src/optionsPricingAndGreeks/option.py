from utilities.optionType import OptionType
from datetime import datetime

class Option:

    def __init__(self, expirationDate: datetime, type: OptionType, strike: float, price = None) -> None:
        self.type = type
        self.expirationDate = expirationDate
        self.strike = strike
        self.price = price

    def calculatePayoff(self, assetPrice):
        return max(assetPrice - self.strike , 0) * -1 if self.type == OptionType.PUT else max(assetPrice - self.strike, 0)


    #useful for debug
    def __str__(self) -> str:
        return f"Type: {self.type.name} - Expiration: {self.expirationDate} - Strike: {self.strike} - Price: {self.price}"