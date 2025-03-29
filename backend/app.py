from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "notebooks"))
from Feature_Extraction import FeatureExtraction  

with open("models/random_forest.pkl", "rb") as model_file:
    forest = pickle.load(model_file)

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict_url():
    data = request.json
    print("Received Data:", data)  

    url = data.get("url", "")
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    features = np.array(FeatureExtraction(url).getFeaturesList()).reshape(1, -1)
    print("Extracted Features:", features)
    print("Feature Shape:", features.shape)
    prediction = forest.predict(features)[0]
    result = "Safe" if prediction == 1 else "Malicious"

    print("Prediction Result:", result)
    return jsonify({"prediction": result})


if __name__ == "__main__":
    app.run(debug=True)