import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

diabetes_df = pd.read_csv("diabetes.csv")
# print(diabetes_df.dtypes)

corr = diabetes_df.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
# sns.pairplot(diabetes_df, hue='Outcome')
plt.show()

diabetes_input = diabetes_df.drop('Outcome', axis=1)
diabetes_output = diabetes_df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(diabetes_input, diabetes_output, test_size=0.2, random_state=42)

std_scaler = StandardScaler()
std_scaler.fit_transform(X_train)
std_scaler.transform(X_test)

logi_model = LogisticRegression(max_iter=500)
logi_model.fit(X_train, y_train)

logi_prediction = logi_model.predict(X_test)
print(logi_prediction)
print("Accuracy:", accuracy_score(y_test, logi_prediction))

# importance = logi_model.coef_[0]
# features = diabetes_input.columns
#
# plt.figure(figsize=(8,5))
# sns.barplot(x=importance, y=features)
# plt.title("Feature Importance (Logistic Regression Coefficients)")
# plt.show()

final_Cross_score = cross_val_score(logi_model, X_train, y_train, cv = 5, scoring="accuracy")
print(final_Cross_score)