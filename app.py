import streamlit as st
import pickle
import numpy as np

# Load the trained model (replace with your actual file name)
model = pickle.load(open("diabetes_model.pkl", "rb"))

st.title("🩺 Diabetes Risk Prediction App")

st.write("Enter your health details below:")

# User Inputs
pregnancies = st.number_input("Pregnancies", 0, 20)
glucose = st.number_input("Glucose", 0, 200)
blood_pressure = st.number_input("Blood Pressure", 0, 140)
bmi = st.number_input("BMI", 0.0, 70.0)
age = st.number_input("Age", 1, 120)

# Add more inputs if needed

# Predict Button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, bmi, age]])
    prediction = model.predict(input_data)[0]
    result = "Diabetic" if prediction == 1 else "Not Diabetic"
    st.success(f"The person is likely: **{result}**")

