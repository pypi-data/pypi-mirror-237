import datetime
from option import Option
from stock import Stock
from utilities.optionType import OptionType
from utilities.period import Period
from utilities.returnsCalculator import ReturnsCalculator
from estimator._estimator import Estimator
import scipy.stats as scipy
import numpy as np

class GreeksEstimator(Estimator):
    def __init__(self, stock: Stock, option: Option, annuallyInterestRate = None, periodForPrices :Period | None = None) -> None:
        super().__init__(stock)
        self.option = option
        
        prices = self.stock.getHistoricalPrices(period=(periodForPrices or self.periodForHistoricalPrices))
        self._actualAssetPrice = prices.iloc[-1]["Close"]

        #days to exoiration
        self._deltaT = (option.expirationDate - datetime.datetime.today()).days / 365

        returnsCalculator = ReturnsCalculator(prices)
        self._sigma = returnsCalculator.dailyVolatilityPercentage * np.sqrt(365)

        #daily interest rate
        self._r = annuallyInterestRate or self.annuallyInterestRate

        #(log(S/E) + (r + (sigma^2)/2)) / (sigma * sqrt(dt))
        self._d1 = np.log(self._actualAssetPrice / self.option.strike) + (self._r + 0.5 * (self._sigma ** 2) * self._deltaT) \
                    / (self._sigma * np.sqrt(self._deltaT))

        #d1 - sigma * sqrt(dt)
        self._d2 = self._d1 - (self._sigma * np.sqrt(self._deltaT))


    @property
    def delta(self):
        if self.option.type == OptionType.CALL:
            #e^{-r * dt}N(d1)
            return np.exp(-self._r * self._deltaT) * scipy.norm.cdf(self._d1)
        #e^{-r * dt}(N(d1) - 1)
        return np.exp(-self._r * self._deltaT) * (scipy.norm.cdf(self._d1) - 1)
    
    @property
    def gamma(self):
        #e^{-r * dt} N'(d1) / (sigma * S * sqrt(dt))
        return np.exp(-self._r * self._deltaT) * scipy.norm.pdf(self._d1) / (self._sigma * self._actualAssetPrice * np.sqrt(self._deltaT))
    
    @property
    def theta(self):
        #- (sigma * S * N'(d1)) / (2 * sqrt(dt)) - r * E * e^{-r * dt} * N(d2)
        argD1 = self._d1 if self.option.type == OptionType.CALL else - self._d1
        argD2 = self._d2 if self.option.type == OptionType.CALL else - self._d2
        
        secondTerm = - self._r * self.option.strike * np.exp(-self._r * self._deltaT) * scipy.norm.cdf(argD2)
        if self.option.type == OptionType.PUT:
            secondTerm *= -1

        return ((-self._sigma * self._actualAssetPrice * scipy.norm.pdf(argD1)) / (2*np.sqrt(self._deltaT))) + secondTerm
    
    @property
    def vega(self):
        #S * e ^{-r * dt} sqrt(dt) * N'(d1)
        return self._actualAssetPrice * np.exp(-self._r * self._deltaT) * np.sqrt(self._deltaT) * scipy.norm.pdf(self._d1)
    
    @property
    def rho(self):
        #E * e^{-r * dt} * N(d1)
        multiplier = 1 if self.option.type == OptionType.CALL else -1
        return multiplier * self.option.strike * self._deltaT * np.exp(-self._r * self._deltaT ) * scipy.norm.cdf(multiplier * self._d2)