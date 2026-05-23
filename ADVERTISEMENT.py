import streamlit as st
import pickle
import numpy as np

# Load model
with open("lr.sav", "rb") as file:
    model = pickle.load(file)

st.title("Sales Prediction App")

# Input Features
TV = st.number_input("TV adv budget", min_value=0.0)
Radio = st.number_input("Radio Adv Budget", min_value=0.0)
Newspaper = st.number_input("Newspaper budget", min_value=0.0)

# Prediction button
if st.button("Predict Sales"):
    input_data = np.array([[TV, Radio, Newspaper]])
    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Sales: {prediction:.2f}")
