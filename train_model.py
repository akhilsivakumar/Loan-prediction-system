import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def preprocess_data(data):
    # Handle missing values
    data['LoanAmount'].fillna(data['LoanAmount'].median(), inplace=True)
    data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0], inplace=True)
    data['Credit_History'].fillna(data['Credit_History'].mode()[0], inplace=True)
    
    # Convert categorical variables to numerical
    categorical_columns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
    data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)
    return data

def train_model(data_path):
    # Load dataset
    data = pd.read_csv(data_path)
    
    # Preprocess data
    data = preprocess_data(data)
    
    # Split features and target
    features = data.drop(columns=['Loan_ID', 'Loan_Status'])
    target = data['Loan_Status'].map({'Y': 1, 'N': 0})  # Convert 'Y' and 'N' to binary labels
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    # Train Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy:.2f}")
    
    # Save the trained model
    joblib.dump(model, 'src/loan_model.pkl')
    print("Model saved successfully!")

if __name__ == "__main__":
    train_model("data/train.csv")
