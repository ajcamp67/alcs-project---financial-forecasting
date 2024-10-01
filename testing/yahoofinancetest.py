import yfinance as yf

spfiveData = yf.Ticker("^GSPC")
# print(spfiveData.info)
print(spfiveData.history(period="max"))
