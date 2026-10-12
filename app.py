from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

MODEL_FILE = "model.pkl"
PIPELINE_FILE = "pipeline.pkl"

# Load model and pipeline once when the server starts
model = joblib.load(MODEL_FILE)
pipeline = joblib.load(PIPELINE_FILE)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        input_data = pd.DataFrame([{
            "longitude": float(data["longitude"]),
            "latitude": float(data["latitude"]),
            "housing_median_age": float(data["housing_median_age"]),
            "total_rooms": float(data["total_rooms"]),
            "total_bedrooms": float(data["total_bedrooms"]),
            "population": float(data["population"]),
            "households": float(data["households"]),
            "median_income": float(data["median_income"]),
            "ocean_proximity": data["ocean_proximity"]
        }])

        # Transform using the saved preprocessing pipeline
        transformed_data = pipeline.transform(input_data)

        # Make prediction
        prediction = model.predict(transformed_data)[0]

        return jsonify({
            "success": True,
            "prediction": round(float(prediction), 2)
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True,port = 5002)