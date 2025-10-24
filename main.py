from flask import Flask, request, jsonify
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Path to the saved model
model_path = os.path.join('app', 'model.pkl')

# Load model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Welcome to the ML Prediction API! Use the /predict endpoint with POST requests."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data)
    predictions = model.predict(df)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
