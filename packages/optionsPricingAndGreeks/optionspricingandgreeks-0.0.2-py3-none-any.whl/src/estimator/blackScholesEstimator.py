import math
from estimator._estimator import Estimator
from option import Option
from utilities.optionType import OptionType
from utilities.period import Period
from utilities.returnsCalculator import ReturnsCalculator
import datetime
import scipy.stats as scipy

class BlackScholesEstimator(Estimator):

    def estimate(self, option: Option, annuallyInterestRate = None, periodForPrices :Period | None = None):
        prices = self.stock.getHistoricalPrices(period=(periodForPrices or self.periodForHistoricalPrices))
        actualAssetPrice = prices.iloc[-1]["Close"]
        
        #days to exoiration
        deltaT = (option.expirationDate - datetime.datetime.today()).days

        returnsCalculator = ReturnsCalculator(prices)
        sigma = returnsCalculator.dailyVolatilityPercentage

        #daily interest rate
        r = (annuallyInterestRate or self.annuallyInterestRate) / 365

        #(log(S/E) + (r + (sigma^2)/2)) / (sigma * sqrt(dt))
        d1 = (math.log(actualAssetPrice / option.strike) + (r + (sigma ** 2 / 2) * deltaT)) \
            / (sigma * math.sqrt(deltaT))

        #d1 - sigma * sqrt(dt)
        d2 = d1 - (sigma * math.sqrt(deltaT))

        #Se^{-D(T-t)}N(d1) - Ee^{r(T - t)}N(d2)
        if option.type == OptionType.CALL:
            return actualAssetPrice * scipy.norm.cdf(d1) - option.strike * (math.e ** -(r * deltaT)) * scipy.norm.cdf(d2)
        
        #-Se^{-D(T-t)}N(d1) + Ee^{r(T - t)}N(d2)
        return - actualAssetPrice * scipy.norm.cdf(d1) + option.strike * (math.e ** -(r * deltaT)) * scipy.norm.cdf(d2)