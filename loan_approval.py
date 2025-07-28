import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load and clean data
df = pd.read_csv("loan.csv")
df.drop("Loan_ID", axis=1, inplace=True)

# Fill missing numeric values
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mean())

# One-hot encoding
df = pd.get_dummies(df, drop_first=True)

# Drop less influential features
less_influential_features = ['Self_Employed_Yes', 'Dependents_1', 'Dependents_2', 'Dependents_3+', 'Gender_Male',
                             'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
df.drop(less_influential_features, axis=1, inplace=True)

# Prepare features and labels
x = df.drop("Loan_Status_Y", axis=1)
y = df["Loan_Status_Y"]

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Evaluate
y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model and feature columns for Flask
with open("loan_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("loan_features.pkl", "wb") as f:
    pickle.dump(x.columns.tolist(), f)
