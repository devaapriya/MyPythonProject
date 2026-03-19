import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("NIFTY_5Y.csv")
print(df.head())
print(df.info())
print(df.columns)
print(df.dtypes)
print(df.describe())
print(df.isnull().sum())

# pct_change() --> This function calculates the percentage change
# between the current row and the previous row.
df['Daily Return'] = df['Close'].pct_change(fill_method=None)
print(df.head())

# Calculate Standard Deviation to calculate Volatility
volatility = df['Daily Return'].std
print('Volatility ', volatility)

plt.plot(df['Close'])
plt.title('Nifty Closing Price')
plt.show()

plt.plot(df['Daily Return'])
plt.title('Daily Return')
plt.show()
