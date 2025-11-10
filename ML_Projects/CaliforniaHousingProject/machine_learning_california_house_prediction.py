import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

# Reading the dataset
df = pd.read_csv('housing.csv')
print(df.head())

# Finding columns with null values
print(df.isnull().sum())

# Fill null values with median
df['total_bedrooms']=df['total_bedrooms'].fillna(df['total_bedrooms'].median())

# One hot encoding categorical field ocean_proximity
df_ocn_prmty = pd.get_dummies(df['ocean_proximity'],drop_first=True)

# Drop ocean_proximity column and concatinate one-hotencoded columns to df
df.drop('ocean_proximity',axis=1, inplace=True)
df = pd.concat([df,df_ocn_prmty], axis=1)

# verifying columns with null values
print(df.isnull().sum())

X = df.drop('median_house_value', axis=1)
y = df['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# std_scaler = StandardScaler()
# std_scaler.fit_transform(X_train)
# std_scaler.transform(X_test)

# Linear Regression Model
lnr_model = LinearRegression()
lnr_model.fit(X_train, y_train)

y_pred_linear = lnr_model.predict(X_test)

r2_score_linear = r2_score(y_test, y_pred_linear)
print("r2_score_linear ",r2_score_linear)

# Random Forest Model
rndm_model = RandomForestRegressor(n_estimators=10)
rndm_model.fit(X_train, y_train)

y_pred_random = rndm_model.predict(X_test)
r2_score_random = r2_score(y_test, y_pred_random)
print("r2_score_random ",r2_score_random)
