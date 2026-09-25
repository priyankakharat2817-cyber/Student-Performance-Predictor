# 🎓 Student Performance Predictor

A Machine Learning project that predicts a student's expected exam score based on **Study Hours, Attendance, and Previous Score**.

The project uses **Python, Pandas, NumPy, Scikit-learn, Matplotlib, Joblib, and Streamlit**.

---

## 📌 About the Project

The **Student Performance Predictor** is a Machine Learning application designed to estimate a student's exam score using important academic factors.

The user provides:

- 📚 Study Hours
- 📅 Attendance Percentage
- 📝 Previous Exam Score

The trained **Linear Regression** model uses these inputs to predict the student's expected exam score.

The model is integrated with a **Streamlit web application**, making it easy for users to enter student information and receive a prediction.

---

## 🎯 Objectives

- Analyze student performance data.
- Clean and prepare the dataset.
- Perform Exploratory Data Analysis (EDA).
- Visualize relationships between different features.
- Train a Machine Learning regression model.
- Evaluate model performance.
- Save the trained model using Joblib.
- Build an interactive Streamlit application.
- Predict student exam scores.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Joblib**
- **Streamlit**
- **Git**
- **GitHub**
- **VS Code**

---

## 📊 Dataset

The dataset contains information about student academic performance.

### Features

| Feature | Description |
|---|---|
| `Study_Hours` | Number of hours the student studies |
| `Attendance` | Student attendance percentage |
| `Previous_Score` | Student's previous exam score |
| `Exam_Score` | Student's exam score |

### Sample Data

| Study Hours | Attendance | Previous Score | Exam Score |
|---:|---:|---:|---:|
| 2 | 60 | 50 | 52 |
| 3 | 65 | 55 | 57 |
| 4 | 70 | 60 | 63 |
| 5 | 75 | 65 | 68 |
| 6 | 80 | 70 | 74 |

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Data Visualization
   ↓
Train-Test Split
   ↓
Linear Regression
   ↓
Model Evaluation
   ↓
Save Model using Joblib
   ↓
Streamlit Web Application
   ↓
Student Inputs
   ↓
Predicted Exam Score
