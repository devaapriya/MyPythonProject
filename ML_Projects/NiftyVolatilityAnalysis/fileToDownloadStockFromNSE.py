import yfinance as yf

nifty = yf.download("^NSEI", period="5y", interval="1d")

nifty.to_csv("NIFTY_5Y.csv")
print(nifty.head())