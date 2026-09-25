import streamlit as st
import joblib
import numpy as np
from pathlib import Path


# Get project folder
project_folder = Path(__file__).resolve().parent

# Model path
model_path = project_folder / "model" / "model.pkl"


# Load trained model
model = joblib.load(model_path)


# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# Title
st.title("🎓 Student Performance Predictor")

st.write(
    "Enter the student's details below to predict "
    "the expected exam score."
)


# Study Hours
study_hours = st.number_input(
    "📚 Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)


# Attendance
attendance = st.number_input(
    "📅 Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0,
    step=1.0
)


# Previous Score
previous_score = st.number_input(
    "📝 Previous Score",
    min_value=0.0,
    max_value=100.0,
    value=60.0,
    step=1.0
)


# Predict button
if st.button("🔮 Predict Exam Score"):

    # Prepare input
    input_data = np.array([
        [study_hours, attendance, previous_score]
    ])

    # Prediction
    prediction = model.predict(input_data)[0]

    # Keep score between 0 and 100
    prediction = max(0, min(100, prediction))


    # Performance category
    if prediction >= 85:
        performance = "Excellent 🌟"

    elif prediction >= 70:
        performance = "Good 👍"

    elif prediction >= 50:
        performance = "Average 🙂"

    else:
        performance = "Needs Improvement 📚"


    # Display result
    st.success(
        f"Predicted Exam Score: {prediction:.2f}"
    )

    st.info(
        f"Performance Level: {performance}"
    )