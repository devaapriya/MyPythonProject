from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle

data = load_breast_cancer()
X = data.data
y = data.target

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.2, random_state=0)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("accuracy_score ", accuracy_score(y_test, y_pred))

# Save model & scaler
pickle.dump(model, open("svc_model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))
print("Model Saved")
