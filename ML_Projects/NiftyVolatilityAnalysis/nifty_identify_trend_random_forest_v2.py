import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("NIFTY_5Y.csv")
print(df.head())

# pct_change() --> This function calculates the percentage change
# between the current row and the previous row.
df['Daily Return'] = df['Close'].pct_change(fill_method=None)
print(df.head())

# Calculate Standard Deviation to calculate Volatility
volatility = df['Daily Return'].std()
print('Volatility ', volatility)

# Identify overall movement in a month 20 days ~ 1 month
df['Volatility'] = df['Daily Return'].rolling(window=20).std()
print('Rolling Volatility ', volatility)

# Calculate Moving Average 20 and 50
df['MA20']=df['Close'].rolling(window=20).mean()
df['MA50']=df['Close'].rolling(window=50).mean()
# print(df.tail())

# Calculate Momentum - if the value is positive then Trend is up else down
df['Momentum'] = df['Close'] - df['Close'].shift(10)
# print(df.tail())
# print(df.columns)

# Calculate RSI to identify Over bought/sold condition
delta = df['Close'].diff()
# print('delta', delta)
gain = (delta.where(delta > 0, 0)).rolling(14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
print('gain', gain)
print('loss', loss)
rs = gain / loss
df['RSI'] = 100 - (100 / (1+rs))
print('RSI', df['RSI'])
print(df.columns)
df = df.dropna()
print(df.columns)
print(df.head())

# Tomorrow Market direction
df['Target'] = df['Close'].shift(-3) > df['Close']
df['Target'] = df['Target'].astype(int)
df = df.dropna()
# print(df[['Close', 'Target']])

# prediction
X = df[[
    "Daily Return",
    "Volatility",
    "MA20",
    "MA50",
    "Momentum",
    "RSI"
]]
y = df['Target']

split = int(len(df) * 0.8)

X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(y_test, y_pred)
print("Accuracy:", accuracy)