import pandas as pd

df=pd.read_csv("titanic.csv")
pd.set_option('display.max_columns', None)
print(df.head())
# print(df.shape)