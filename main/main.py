import pandas as pd
import numpy as np
import customtkinter as ctk
import yfinance as yf
import matplotlib.pyplot as plt

# STOCK VARIABLES
GSPC = ''
GSPC_history = ''
# COMMODITY VARIABLES
gold = ''
goldHistory = ''

# Fetch data on financial instruments
GSPC = yf.Ticker('^GSPC')
GSPC_history = GSPC.history(period="max")
GSPC_history = pd.DataFrame(GSPC_history)

gold = yf.Ticker('GC=F')
goldHistory = gold.history(period="max")
goldHistory = pd.DataFrame(goldHistory)

# Create CSVs for financial instruments
GSPC_history.to_csv('S&P500history.csv')
goldHistory.to_csv('goldHistory.csv')

