import math
from estimator._estimator import Estimator
from option import Option
from stock import Stock
from utilities.period import Period
from utilities.returnsCalculator import ReturnsCalculator
import numpy.random as nprnd
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np


class BootstrapEstimator(Estimator):

    def __init__(self, stock: Stock) -> None:
        super().__init__(stock)
        self._allSimulationPaths = pd.DataFrame([])

    def estimate(self, option: Option, numberOfSimulations = 100, annuallyInterestRate: float | None = None, showSimulationPaths = False, periodForPrices :Period | None = None):
        prices = self.stock.getHistoricalPrices(period=(periodForPrices or self.periodForHistoricalPrices))
        actualAssetPrice = prices.iloc[-1]["Close"]
        
        #days to exoiration
        deltaT = (option.expirationDate - datetime.datetime.today()).days

        returnsCalculator = ReturnsCalculator(prices)
        returns = returnsCalculator.returns

        #daily interest rate
        r = (annuallyInterestRate or self.annuallyInterestRate) / 365

        rng = nprnd.default_rng() 
        
        allSimulationsFinalPrice = np.array([])
        allSimulationPaths = pd.DataFrame()

        for i in range(0, numberOfSimulations):
            price = actualAssetPrice
            simulation = np.array([price])
            
            for _ in range(0, deltaT):
                #add a random past return to the current price
                randomIndex = rng.uniform(0, len(returns))
                price += returns[int(randomIndex)]
                
                simulation = np.append(simulation, price)

            allSimulationsFinalPrice = np.append(allSimulationsFinalPrice, price)

            allSimulationPaths[i] = simulation

        self._allSimulationPaths = allSimulationPaths

        if showSimulationPaths:
            plot = allSimulationPaths.plot.line()
            plot.axes.axes.set_xlabel("Days")
            plot.axes.axes.set_ylabel("Stock price")
            plot.get_legend().remove()
            plt.show()

        #payoff discounted to the actual date
        tot = sum([option.calculatePayoff(finalPrice) * (math.e ** -(r * deltaT)) for finalPrice in allSimulationsFinalPrice ])

        #average
        return tot / len(allSimulationsFinalPrice)
    
    @property
    def simulationPaths(self):
        return self._allSimulationPaths


        