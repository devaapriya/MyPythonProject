import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix)
from sklearn import tree

df=pd.read_csv("titanic.csv")
pd.set_option('display.max_columns', None)
# print(df.head())
# print(df.shape)
# print(df.columns)

input_columns=df[["Pclass","Sex", "Age", "Fare"]].copy()
target_column=df["Survived"]

label_encoder_object = LabelEncoder()
input_columns['Sex'] = label_encoder_object.fit_transform(input_columns['Sex'])

# null check
# print(input_columns.isnull().sum())
# print(input_columns[:10])
input_columns['Age']=input_columns['Age'].fillna(input_columns['Age'].mean())
# print(input_columns[:10])
# print(input_columns.isnull().sum())

X_train, X_test, y_train, y_test = train_test_split(input_columns, target_column, test_size=0.2, random_state=42)
print("X_train",len(X_train))
print("X_test", len(X_test))

classifier = tree.DecisionTreeClassifier(max_depth=3)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Calculate score
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
confusion_matrix = confusion_matrix(y_test, y_pred)

# print the results
print(f"Accuracy: {accuracy}")
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print(confusion_matrix)

# plot the tree
plt.figure(figsize=(15,8))
tree.plot_tree(classifier,filled=True,
    rounded=True,
    fontsize=10,
    impurity=True)
plt.show()