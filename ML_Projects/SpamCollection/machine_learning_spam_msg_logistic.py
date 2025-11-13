import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("spam.csv", encoding="latin-1")
# print(df.head())
# print(df.shape)
# print(df.info())
print("null values ",df.isnull().sum())
print("duplicated ",df.duplicated())

df = df[['v1', 'v2']]
print(df.head())
print(df.shape)
# print(df.info())

labelEncoder = LabelEncoder()
df['v1'] = labelEncoder.fit_transform(df['v1'])
print(df.head())

X = df['v2']
y = df['v1']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(X_train.shape)
print(X_test.shape)

tfidfVectorizer = TfidfVectorizer(max_features=3000)
X_train_vector = tfidfVectorizer.fit_transform(X_train)
X_test_vector = tfidfVectorizer.transform(X_test)

logisticRegressionModel = LogisticRegression()
logisticRegressionModel.fit(X_train_vector, y_train)

y_pred = logisticRegressionModel.predict(X_test_vector)

print("Accuracy ", accuracy_score(y_test, y_pred))
print("confusion_matrix\n", confusion_matrix(y_test, y_pred))
print("classification_report\n", classification_report(y_test, y_pred))
