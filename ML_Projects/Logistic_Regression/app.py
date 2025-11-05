from flask import Flask, request, jsonify
import pickle
import pandas as pd

with open("logistic_trained_csv_model.pkl","rb") as file_read_obj:
    train_model=pickle.load(file_read_obj)

my_app = Flask(__name__)

@my_app.route("/")
def landing():
    return "Welcome to Logistics"

@my_app.route("/login", methods=["POST"])
def login():
    return jsonify({"message": "Flask is working!"})

@my_app.route("/logistic_trained_csv_prediction", methods=["POST"])
def logistics_prediction():
    data = request.get_json()
    print("data ***** ",data)
    Pregnancies = data.get("Pregnancies")
    Glucose = data.get("Glucose")
    BloodPressure = data.get("BloodPressure")
    SkinThickness = data.get("SkinThickness")
    Insulin = data.get("Insulin")
    BMI = data.get("BMI")
    DiabetesPedigreeFunction = data.get("DiabetesPedigreeFunction")
    Age = data.get("Age")
    # if not year_in_req or not isinstance(year_in_req, list):
    #     return jsonify({'Error: Check your input'}), 400

    # predictions = train_model.predict(year_in_req)
    data_input = pd.DataFrame({"Pregnancies":Pregnancies,
                               "Glucose":Glucose,
                               "BloodPressure":BloodPressure,
                               "SkinThickness":SkinThickness,
                               "Insulin":Insulin,
                               "BMI":BMI,
                               "DiabetesPedigreeFunction":DiabetesPedigreeFunction,
                               "Age":Age})
    predictions = train_model.predict(data_input[["Pregnancies",
                                                  "Glucose",
                                                  "BloodPressure",
                                                  "SkinThickness",
                                                  "Insulin",
                                                  "BMI",
                                                  "DiabetesPedigreeFunction",
                                                  "Age"]])
    return jsonify({'prediction': predictions.tolist()})
    # return jsonify({"message": "Flask is working!"})

if __name__ == "__main__":
    my_app.run(debug=True)
