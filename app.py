import streamlit as st
import requests



st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="centered")
st.title("💓 Heart Disease Prediction App")
st.markdown("Enter the patient's details below. The model will predict the risk of heart disease.")

with st.sidebar:
    st.header("📝 Feature Explanations")
    st.markdown("""
    **Age**: Age of the patient (years). Typical: 29–77.
    
    **Sex**: 0 = Female, 1 = Male.
    
    **Chest Pain Type (cp)**: 0: Typical angina, 1: Atypical angina, 2: Non-anginal pain, 3: Asymptomatic.
    
    **Resting Blood Pressure (trestbps)**: Resting blood pressure (mm Hg). Typical: 90–200.
    
    **Serum Cholesterol (chol)**: Serum cholesterol (mg/dl). Typical: 125–564.
    
    **Fasting Blood Sugar (fbs)**: 1 = Fasting blood sugar > 120 mg/dl, 0 = otherwise.
    
    **Resting ECG (restecg)**: 0: Normal, 1: ST-T wave abnormality, 2: Left ventricular hypertrophy.
    
    **Max Heart Rate Achieved (thalach)**: Maximum heart rate achieved. Typical: 70–210.
    
    **Exercise-Induced Angina (exang)**: 1 = Yes, 0 = No.
    
    **ST Depression (oldpeak)**: ST depression induced by exercise relative to rest. Typical: 0–6.2.
    
    **Slope of Peak Exercise ST Segment (slope)**: 0: Upsloping, 1: Flat, 2: Downsloping.
    
    **Number of Major Vessels (ca)**: Number of major vessels colored by fluoroscopy (0–3). Typical: 0–4.
    
    **Thalassemia (thal)**: 1: Normal, 2: Fixed defect, 3: Reversible defect.
    """)

with st.form("heart_form"):
    age = st.number_input("Age", min_value=20, max_value=100, value=50)
    sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3], format_func=lambda x: ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"][x])
    trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=220, value=120)
    chol = st.number_input("Serum Cholesterol", min_value=100, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar", [0, 1], format_func=lambda x: "≤ 120 mg/dl" if x == 0 else "> 120 mg/dl")
    restecg = st.selectbox("Resting ECG", [0, 1, 2], format_func=lambda x: ["Normal", "ST-T abnormality", "LVH"][x])
    thalach = st.number_input("Max Heart Rate", min_value=60, max_value=220, value=150)
    exang = st.selectbox("Exercise-Induced Angina", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=7.0, value=1.0, step=0.1)
    slope = st.selectbox("Slope", [0, 1, 2], format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x])
    ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thalassemia", [1, 2, 3], format_func=lambda x: ["Normal", "Fixed defect", "Reversible defect"][x-1])
    submitted = st.form_submit_button("Predict")

if submitted:
    data = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }
    try:
        response = requests.post("http://localhost:8000/predict", json=data)
        if response.status_code == 200:
            pred = response.json()["prediction"]
            if pred == 1:
                st.success("🚨 The model predicts a high risk of heart disease.")
            else:
                st.success("✅ The model predicts a low risk of heart disease.")
        else:
            st.error("Prediction failed. Please check the API server.")
    except Exception as e:
        st.error(f"Error: {e}")
