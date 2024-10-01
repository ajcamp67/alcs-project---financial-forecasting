import yfinance as yf
import pandas as pd
import numpy as np

spfiveData = yf.Ticker("^GSPC")
# print(spfiveData.info)
# print(spfiveData.history(period="ytd"))
spfiveHistory = spfiveData.history(period="ytd")
spfiveHistory = pd.DataFrame(spfiveHistory)
print(spfiveHistory)
spfiveHistory.to_csv('SP500.csv')
