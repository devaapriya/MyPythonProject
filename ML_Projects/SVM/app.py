from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model & scaler
model = pickle.load(open("svc_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return "Flask SVM API is running successfully on Azure!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]   # Expect list of 30 values
    data = np.array(data).reshape(1, -1)
    data = scaler.transform(data)

    prediction = model.predict(data)

    result = "Benign (Safe)" if prediction[0] == 1 else "Malignant (Risk)"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)