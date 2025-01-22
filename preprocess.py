import pandas as pd

def preprocess_data(data):
    # Fill missing values
    data['LoanAmount'].fillna(data['LoanAmount'].median(), inplace=True)
    data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0], inplace=True)
    data['Credit_History'].fillna(data['Credit_History'].mode()[0], inplace=True)
    
    # Encode categorical variables
    categorical_columns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
    data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)
    
    return data
