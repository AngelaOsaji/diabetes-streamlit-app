import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page title
st.set_page_config(page_title="Diabetes Risk Predictor", layout="centered")
st.title("🩺 Diabetes Risk Prediction App")
st.markdown("Enter patient details to predict diabetes risk.")

# Input fields — only 6 features (no SkinThickness, no Insulin)
st.markdown("### 🧾 Patient Health Information")

pregnancies = st.number_input(
    "Pregnancies (0–20)",
    min_value=0, max_value=20,
    help="Number of times the patient has been pregnant"
)

glucose = st.number_input(
    "Glucose (mg/dL, 0–200)",
    min_value=0, max_value=200,
    help="Plasma glucose concentration (mg/dL)"
)

blood_pressure = st.number_input(
    "Blood Pressure (mm Hg, 0–140)",
    min_value=0, max_value=140,
    help="Diastolic blood pressure in mm Hg"
)

bmi = st.number_input(
    "BMI (kg/m², 0.0–70.0)",
    min_value=0.0, max_value=70.0,
    help="Body Mass Index (weight in kg / height in m²)"
)

diabetes_pedigree = st.number_input(
    "Diabetes Pedigree Function (0.0–2.5)",
    min_value=0.0, max_value=2.5,
    help="Function indicating family history of diabetes"
)

age = st.number_input(
    "Age (years, 1–120)",
    min_value=1, max_value=120,
    help="Age of the individual"
)

# Predict button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, bmi, diabetes_pedigree, age]])
    prediction = model.predict(input_data)[0]

    st.markdown("---")
    if prediction == 1:
        st.error("⚠️ The model predicts this individual is at **high risk** of diabetes.")
    else:
        st.success("✅ The model predicts this individual is **not likely** to have diabetes.")

# Footer
st.markdown("---")
st.caption("Built by Angela Osaji • Powered by Streamlit and scikit-learn")
