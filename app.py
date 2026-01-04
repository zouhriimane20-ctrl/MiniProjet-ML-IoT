import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("final_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("IoT Intrusion Detection System")

st.write("Enter network traffic features to predict the type of traffic.")

# Example inputs (you can adapt number if needed)
feature_1 = st.number_input("Feature 1", value=0.0)
feature_2 = st.number_input("Feature 2", value=0.0)
feature_3 = st.number_input("Feature 3", value=0.0)
feature_4 = st.number_input("Feature 4", value=0.0)

if st.button("Predict"):
    input_data = np.array([[feature_1, feature_2, feature_3, feature_4]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Class: {prediction[0]}")
