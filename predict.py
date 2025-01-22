import pandas as pd
import joblib
from src.preprocess import preprocess_data

def predict_loan_eligibility(input_data):
    """
    Predict loan eligibility based on user input data.
    
    Parameters:
        input_data (dict): A dictionary containing user inputs with keys as feature names.
        
    Returns:
        str: Prediction result ("Eligible" or "Not Eligible").
    """
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Preprocess the data
    input_df = preprocess_data(input_df)
    
    # Load the trained model
    model = joblib.load('src/loan_model.pkl')
    
    # Make prediction
    prediction = model.predict(input_df)
    
    # Convert numeric prediction to human-readable result
    result = "Eligible" if prediction[0] == 1 else "Not Eligible"
    
    return result

# Example usage
if __name__ == "__main__":
    # Example input data
    sample_input = {
        "Gender": "Male",
        "Married": "Yes",
        "Dependents": "1",
        "Education": "Graduate",
        "Self_Employed": "No",
        "ApplicantIncome": 5000,
        "CoapplicantIncome": 2000,
        "LoanAmount": 150,
        "Loan_Amount_Term": 360,
        "Credit_History": 1.0,
        "Property_Area": "Urban"
    }
    
    # Predict loan eligibility
    result = predict_loan_eligibility(sample_input)
    print(f"Loan Eligibility Prediction: {result}")
