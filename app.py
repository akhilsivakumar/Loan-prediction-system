from flask import Flask, request, jsonify
import joblib
import pandas as pd
from src.preprocess import preprocess_data

app = Flask(__name__)
model = joblib.load('src/loan_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data
        data = request.get_json()
        input_data = pd.DataFrame([data])
        
        # Preprocess input
        input_data = preprocess_data(input_data)
        
        # Predict using the loaded model
        prediction = model.predict(input_data)
        result = "Eligible" if prediction[0] == 1 else "Not Eligible"
        
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
