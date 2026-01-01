# app.py
import streamlit as st
import joblib
import numpy as np

# Load model and encoder
model = joblib.load('disease_model.pkl')
mlb = joblib.load('symptom_encoder.pkl')

# Streamlit UI
st.set_page_config(page_title="Disease Predictor", layout="centered")
st.title("🩺 Disease Prediction from Symptoms")

st.markdown("Select the symptoms you are experiencing:")

# Get all possible symptoms from encoder
all_symptoms = sorted(mlb.classes_.tolist())

# Multi-select box for symptoms
selected_symptoms = st.multiselect("Symptoms", all_symptoms)

# Predict button
if st.button("Predict Disease"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        # Convert selected symptoms into model input
        input_vector = mlb.transform([selected_symptoms])
        prediction = model.predict(input_vector)[0]

        st.success(f"✅ Predicted Disease: **{prediction}**")
