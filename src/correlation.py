import pandas as pd
from pathlib import Path

# Get project folder
project_folder = Path(__file__).resolve().parent.parent

# Dataset path
dataset_path = project_folder / "dataset" / "student_data.csv"

# Load dataset
df = pd.read_csv(dataset_path)

# Calculate correlation
correlation = df.corr(numeric_only=True)

print("Correlation Matrix:")
print(correlation)