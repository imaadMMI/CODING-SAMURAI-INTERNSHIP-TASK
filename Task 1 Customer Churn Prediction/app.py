# Gender: 1 -> Female , 0 -> Male
# Churn: 1 -> Yes, 0 -> No
# Scaler is exported as scaler.pkl
# Model is exported as model.pkl
# Order of the x -> 'Age', 'Gender', 'MonthlyCharges', 'Tenure'

import joblib
import streamlit as st
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Customer Churn Prediction")

st.divider()

st.write("Please enter the following details to predict if a customer is likely to churn:")
st.write("Hit predict for getting the prediction!")

st.divider()

age = st.number_input("Enter the Age", min_value=10, max_value=100, value=30)

tenure = st.number_input("Enter the Tenure (in months)", min_value=0, max_value=130, value=10)

monthly_charges = st.number_input("Enter the Monthly Charges", min_value=0.0, max_value=150.0)

gender = st.selectbox("Enter the Gender", ["Male", "Female"])

st.divider()

predictButton = st.button("Predict Churn")

st.divider()

if predictButton:

    gender_selected = 1 if gender == "Female" else 0

    X = [age, gender_selected, monthly_charges, tenure] 

    X1 = np.array(X)

    X_array = scaler.transform([X1])

    prediction = model.predict(X_array)[0]

    predicted = "Churn" if prediction == 1 else "Not Churn"

    st.balloons()

    st.write(f"The predicted result is: {predicted}")

else:
    st.write("Please fill in all the details and hit predict!")
