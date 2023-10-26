import pandas as pd

class ReturnsCalculator:

    def __init__(self, prices: pd.DataFrame) -> None:
        self._df = prices.reset_index()

        pricesPlusOneDay = self._df[1:].reset_index()
        self.returns = (pricesPlusOneDay["Close"] - self._df[:-1]["Close"]) / self._df[:-1]["Close"]

    @property
    def dailyVolatilityPercentage(self):
        return self.returns.std()
    
    @property
    def dailyDriftPercentage(self):
        return self.returns.mean()

if __name__ == "__main__":
    import yfinance as yf
    x = yf.Ticker("AAPL").history()
    print(ReturnsCalculator(x).dailyDriftPercentage)