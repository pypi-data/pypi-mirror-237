from enum import Enum

class Period(Enum):
    D1 = "1d"
    D5 = "5d"
    M1 = "1mo"
    M3 = "3mo"
    M6 = "6mo"
    Y1 = "1y"
    Y2 = "2y"
    Y5 = "5y"
    Y10 = "10y"
    YTD = "ytd"
    MAX = "max "