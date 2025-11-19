import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

df=pd.read_csv('StudentsPerformance.csv')
df.head()

X = df.drop('math score', axis=1)
y = df['math score']
df.info()

num_cols = X.select_dtypes(exclude="object").columns
cat_cols = X.select_dtypes(include="object").columns

print("num_cols ",num_cols)
print("cat_cols ",cat_cols)

std_scaler = StandardScaler()
ohe = OneHotEncoder()

preprocessor = ColumnTransformer(
    [
        ("OneHotEncoder", ohe, cat_cols),
        ("StandardScaler", std_scaler, num_cols)
    ]
)

X = preprocessor.fit_transform(X)
# print(X)
# print("shape ",X.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# X_train_scaled = sc.fit_transform(X_train)
# X_test_scaled = sc.transform(X_test)
#
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
print(r2)



