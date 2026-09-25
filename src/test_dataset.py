import pandas as pd
from pathlib import Path

# Get the main project folder
project_folder = Path(__file__).resolve().parent.parent

# Create the complete path to the dataset
dataset_path = project_folder / "dataset" / "student_data.csv"

# Load the dataset
df = pd.read_csv(dataset_path)

# Display the dataset
print(df)