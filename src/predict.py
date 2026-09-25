import joblib
from pathlib import Path


# ==========================================
# 1. Get project folder
# ==========================================

project_folder = Path(__file__).resolve().parent.parent


# ==========================================
# 2. Model path
# ==========================================

model_path = project_folder / "model" / "model.pkl"


# ==========================================
# 3. Load trained model
# ==========================================

model = joblib.load(model_path)

print("Student Performance Predictor")
print("--------------------------------")


# ==========================================
# 4. Take input from user
# ==========================================

study_hours = float(input("Enter study hours: "))

attendance = float(input("Enter attendance percentage: "))

previous_score = float(input("Enter previous score: "))


# ==========================================
# 5. Create student data
# ==========================================

student_data = [[
    study_hours,
    attendance,
    previous_score
]]


# ==========================================
# 6. Predict exam score
# ==========================================

prediction = model.predict(student_data)


# ==========================================
# 7. Display prediction
# ==========================================

print("\n--------------------------------")
print(f"Predicted Exam Score: {prediction[0]:.2f}")
print("--------------------------------")