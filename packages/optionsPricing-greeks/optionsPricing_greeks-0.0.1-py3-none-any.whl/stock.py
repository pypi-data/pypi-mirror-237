import yfinance as yf
from option import Option
from utilities.interval import Interval
from utilities.optionType import OptionType
from utilities.period import Period
import pandas as pd
from datetime import datetime

class Stock:

    def __init__(self, symbol) -> None:
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    def getHistoricalPrices(self, period: Period = Period.MAX, interval :Interval = Interval.d1) -> pd.DataFrame : 
        return self.ticker.history(period= period.value, interval= interval.value)

    def possibleOptionExpirationDays(self):
        return self.ticker.options

    def getCallOptions(self, date) -> list[Option]:
        result = []
        for _, option in self.ticker.option_chain(date= date).calls.iterrows():
            result.append(Option(
                type=OptionType.CALL,
                strike=option["strike"],
                expirationDate= datetime.strptime(date, "%Y-%m-%d"),
                price= option["lastPrice"]
            ))
        return result
    
    def getPutOptions(self, date) -> list[Option]:
        result = []
        for _, option in self.ticker.option_chain(date= date).puts.iterrows():
            result.append(Option(
                type=OptionType.PUT,
                strike=option["strike"],
                expirationDate= datetime.strptime(date, "%Y-%m-%d"),
                price= option["lastPrice"]
            ))
        return result
