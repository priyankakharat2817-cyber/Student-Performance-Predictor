import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==========================================
# 1. Get project folder
# ==========================================

project_folder = Path(__file__).resolve().parent.parent


# ==========================================
# 2. Dataset path
# ==========================================

dataset_path = project_folder / "dataset" / "student_data.csv"


# ==========================================
# 3. Load dataset
# ==========================================

df = pd.read_csv(dataset_path)

print("Dataset loaded successfully!")
print(df.head())


# ==========================================
# 4. Select Features and Target
# ==========================================

X = df[["Study_Hours", "Attendance", "Previous_Score"]]

y = df["Exam_Score"]


# ==========================================
# 5. Split dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\nTraining data:", len(X_train))
print("Testing data:", len(X_test))


# ==========================================
# 6. Create Linear Regression model
# ==========================================

model = LinearRegression()


# ==========================================
# 7. Train model
# ==========================================

model.fit(X_train, y_train)

print("\nModel trained successfully!")


# ==========================================
# 8. Make predictions
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 9. Evaluate model
# ==========================================

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)


print("\nModel Performance:")
print("----------------------------")
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)


# ==========================================
# 10. Compare actual and predicted values
# ==========================================

print("\nActual vs Predicted:")
print("----------------------------")

for actual, predicted in zip(y_test, y_pred):
    print(
        f"Actual: {actual:.2f} | "
        f"Predicted: {predicted:.2f}"
    )


# ==========================================
# 11. Save trained model
# ==========================================

model_path = project_folder / "model" / "model.pkl"

joblib.dump(model, model_path)

print("\nModel saved successfully!")
print("Location:", model_path)