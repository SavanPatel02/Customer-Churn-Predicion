import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved objects
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("model_columns.pkl")

st.title("📉 Customer Churn Prediction Dashboard")

st.write("Predict whether a customer is likely to churn")

# User input form
user_data = {}

for col in columns:
    user_data[col] = st.number_input(col, value=0.0)

# Convert input to DataFrame
input_df = pd.DataFrame([user_data])

# Scale input
input_scaled = scaler.transform(input_df)

# Prediction
if st.button("Predict Churn"):
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Customer will CHURN (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Customer will NOT churn (Probability: {probability:.2f})")
