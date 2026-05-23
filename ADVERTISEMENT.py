import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("lr.pkl")

st.title("Sales Prediction App")

TV = st.number_input("TV Advertising Budget", min_value=0.0)
Radio = st.number_input("Radio Advertising Budget", min_value=0.0)
Newspaper = st.number_input("Newspaper Advertising Budget", min_value=0.0)

if st.button("Predict Sales"):
    input_data = np.array([[TV, Radio, Newspaper]])

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Sales: {prediction:.2f}")
