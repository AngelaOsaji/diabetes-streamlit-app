import streamlit as st
import pickle
import numpy as np

# Load the trained model (replace with your actual file name)
model = pickle.load(open("diabetes_model.pkl", "rb"))

st.title("🩺 Diabetes Risk Prediction App")

st.write("Enter your health details below:")

# User Inputs


st.markdown("### 🧾 Patient Health Information")

pregnancies = st.number_input("Pregnancies (0–20)", min_value=0, max_value=20)
glucose = st.number_input("Glucose (mg/dL, 0–200)", min_value=0, max_value=200)
blood_pressure = st.number_input("Blood Pressure (mm Hg, 0–140)", min_value=0, max_value=140)
skin_thickness = st.number_input("Skin Thickness (mm, 0–100)", min_value=0, max_value=100)
insulin = st.number_input("Insulin (μU/mL, 0–900)", min_value=0, max_value=900)
bmi = st.number_input("BMI (kg/m², 0.0–70.0)", min_value=0.0, max_value=70.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function (0.0–2.5)", min_value=0.0, max_value=2.5)
age = st.number_input("Age (years, 1–120)", min_value=1, max_value=120)


# Add more inputs if needed

# Predict Button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, bmi, age]])
    prediction = model.predict(input_data)[0]
    result = "Diabetic" if prediction == 1 else "Not Diabetic"
    st.success(f"The person is likely: **{result}**")

