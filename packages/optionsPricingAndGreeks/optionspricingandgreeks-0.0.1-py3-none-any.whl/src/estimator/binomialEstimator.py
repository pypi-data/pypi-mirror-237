from estimator._estimator import Estimator
import math
from utilities.period import Period
from utilities.returnsCalculator import ReturnsCalculator
from option import Option
import datetime
import numpy as np

class BinomialEstimator(Estimator):
    
    def estimate(self, option: Option, annuallyInterestRate = None, periodForPrices :Period | None = None):
        prices = self.stock.getHistoricalPrices(period=(periodForPrices or self.periodForHistoricalPrices))
        actualAssetPrice = prices.iloc[-1]["Close"]

        returnsCalculator = ReturnsCalculator(prices)
        sigma = returnsCalculator.dailyVolatilityPercentage
        
        #days to exoiration
        deltaT = (option.expirationDate - datetime.datetime.today()).days
        
        #daily interest rate
        r = (annuallyInterestRate or self.annuallyInterestRate) / 365

        u =  1 + sigma 
        d =  1 - sigma 

        #p' = 0.5 + (r * sqrt(deltaT) / 2 sigma)
        riskNeutralProbability =  0.5 + (r * (math.sqrt(deltaT))) / (2*sigma)

        finalPricesForTheOption = []

        for increasesTimes in range(deltaT, 0, -1):
            decreasesTimes = deltaT - increasesTimes
            finalPricesForTheOption.append(
                #S * u^p * d^q
                actualAssetPrice * (u ** increasesTimes) * (d ** decreasesTimes) 
            )

        #leafes of the tree for the option value
        valuesAtEachStep = [option.calculatePayoff(finalPrice) for finalPrice in finalPricesForTheOption]

        while len(valuesAtEachStep) > 1:
            result = []
            normal = valuesAtEachStep[:-1]
            oneBehind = valuesAtEachStep[1:]

            for VPlus, VMinus in zip(normal, oneBehind):
                #V = (p * V^+ + (1-p) * V^-) * e^{-r * dt}
                VOneStepEarlier = (riskNeutralProbability * VPlus + (1 - riskNeutralProbability) * VMinus) * math.exp(-r * deltaT)
                result.append(VOneStepEarlier)

            valuesAtEachStep = result.copy()

        return valuesAtEachStep[0]
    
    def estimateAmericanOption(self, option: Option, annuallyInterestRate = None, periodForPrices :Period | None = None):
        prices = self.stock.getHistoricalPrices(period=(periodForPrices or self.periodForHistoricalPrices))
        actualAssetPrice = prices.iloc[-1]["Close"]

        returnsCalculator = ReturnsCalculator(prices)
        sigma = returnsCalculator.dailyVolatilityPercentage
        
        #days to exoiration
        deltaT = (option.expirationDate - datetime.datetime.today()).days
        
        #daily interest rate
        r = (annuallyInterestRate or self.annuallyInterestRate) / 365

        u =  1 + sigma
        d =  1 - sigma

        print(sigma)

        #p' = 0.5 + (r * sqrt(deltaT) / 2 sigma)
        riskNeutralProbability = 0.5 + (r * (math.sqrt(deltaT))) / (2*sigma)

        binomialTree = []

        for days in range(2, deltaT):
            pricesForOneTreeLevel = []
            for increasesTimes in range(days, 0, -1):
                decreasesTimes = deltaT - increasesTimes
                pricesForOneTreeLevel.append(
                    #S * u^p * d^q
                    actualAssetPrice * (u ** increasesTimes) * (d ** decreasesTimes) 
                )

            binomialTree.append(pricesForOneTreeLevel)
        
        #leafes of the tree for the option value
        valuesAtEachStep = [option.calculatePayoff(finalPrice) for finalPrice in binomialTree[-1]]

        treeLevel = 0

        #the option values shouldn't go below the payoff, otherwise arbitrage opportunity
        while len(valuesAtEachStep) > 1:
            treeLevel -= 1
            result = []
            normal = valuesAtEachStep[:-1]
            oneBehind = valuesAtEachStep[1:]

            for index, (VPlus, VMinus) in enumerate(zip(normal, oneBehind)):
                #V = (p * V^+ + (1-p) * V^-) * discountRate
                VOneStepEarlier = (riskNeutralProbability * VPlus + (1 - riskNeutralProbability) * VMinus) * math.exp(-r * deltaT) 
                VOneStepEarlier = max(VOneStepEarlier, option.calculatePayoff(binomialTree[treeLevel][index]) )
                result.append(VOneStepEarlier)

            valuesAtEachStep = result.copy()

        return valuesAtEachStep[0]






