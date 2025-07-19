import streamlit as st
import pickle
import numpy as np

# Load the trained model (replace with your actual file name)
model = pickle.load(open("diabetes_model.pkl", "rb"))

st.title("🩺 Diabetes Risk Prediction App")

st.write("Enter your health details below:")

# User Inputs


pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, help="Number of times pregnant")
glucose = st.number_input("Glucose (mg/dL)", min_value=0, max_value=200, help="Plasma glucose concentration")
blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=140, help="Diastolic blood pressure (mm Hg)")
skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, help="Triceps skin fold thickness")
insulin = st.number_input("Insulin (μU/mL)", min_value=0, max_value=900, help="2-Hour serum insulin level")
bmi = st.number_input("BMI (kg/m²)", min_value=0.0, max_value=70.0, help="Body Mass Index")
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, help="Function scores genetic risk")
age = st.number_input("Age (years)", min_value=1, max_value=120, help="Age of the person")


# Add more inputs if needed

# Predict Button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, bmi, age]])
    prediction = model.predict(input_data)[0]
    result = "Diabetic" if prediction == 1 else "Not Diabetic"
    st.success(f"The person is likely: **{result}**")

