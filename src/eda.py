import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Paths
dataset_path = project_folder / "dataset" / "student_data.csv"
graph_folder = project_folder / "graphs"

# Load dataset
df = pd.read_csv(dataset_path)

print("Dataset loaded successfully!")


# ==========================================
# Graph 1: Study Hours vs Exam Score
# ==========================================

plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Exam_Score"])

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")

plt.tight_layout()
plt.savefig(graph_folder / "study_hours_vs_score.png")
plt.close()

print("Study Hours graph saved!")


# ==========================================
# Graph 2: Attendance vs Exam Score
# ==========================================

plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance"], df["Exam_Score"])

plt.xlabel("Attendance (%)")
plt.ylabel("Exam Score")
plt.title("Attendance vs Exam Score")

plt.tight_layout()
plt.savefig(graph_folder / "attendance_vs_score.png")
plt.close()

print("Attendance graph saved!")


# ==========================================
# Graph 3: Previous Score vs Exam Score
# ==========================================

plt.figure(figsize=(8, 5))
plt.scatter(df["Previous_Score"], df["Exam_Score"])

plt.xlabel("Previous Score")
plt.ylabel("Exam Score")
plt.title("Previous Score vs Exam Score")

plt.tight_layout()
plt.savefig(graph_folder / "previous_score_vs_score.png")
plt.close()

print("Previous Score graph saved!")


print("\nAll EDA graphs created successfully!")