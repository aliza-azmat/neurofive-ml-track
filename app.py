
import streamlit as st
import pandas as pd
import joblib

# Load the trained model and encoders
model = joblib.load("titanic_random_forest.pkl")
sex_encoder = joblib.load("sex_encoder.pkl")
embarked_encoder = joblib.load("embarked_encoder.pkl")

# App title
st.title("🚢 Titanic Survival Prediction")

st.write(
    "Enter the passenger details below to predict whether "
    "the passenger would survive."
)

# Input fields
pclass = st.selectbox(
    "Passenger Class",
    [1, 2, 3]
)

sex = st.selectbox(
    "Sex",
    ["female", "male"]
)

age = st.number_input(
    "Age",
    min_value=0.0,
    max_value=100.0,
    value=30.0
)

sibsp = st.number_input(
    "Number of Siblings/Spouses",
    min_value=0,
    max_value=10,
    value=0
)

parch = st.number_input(
    "Number of Parents/Children",
    min_value=0,
    max_value=10,
    value=0
)

fare = st.number_input(
    "Fare",
    min_value=0.0,
    value=30.0
)

embarked = st.selectbox(
    "Port of Embarkation",
    ["C", "Q", "S"]
)

# Prediction button
if st.button("Predict Survival"):

    # Encode categorical inputs
    sex_encoded = sex_encoder.transform([sex])[0]
    embarked_encoded = embarked_encoder.transform([embarked])[0]

    # Create input dataframe
    input_data = pd.DataFrame({
        "Pclass": [pclass],
        "Sex": [sex_encoded],
        "Age": [age],
        "SibSp": [sibsp],
        "Parch": [parch],
        "Fare": [fare],
        "Embarked": [embarked_encoded]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == 1:
        st.success("✅ Prediction: The passenger is likely to survive.")
    else:
        st.error("❌ Prediction: The passenger is unlikely to survive.")
