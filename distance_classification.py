import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset (replace with actual dataset path)
try:
    df = pd.read_csv("dataset.csv")  # Ensure dataset.csv exists in the project directory
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    print("Dataset loaded and split successfully!")
except FileNotFoundError:
    print("Error: dataset.csv not found. Please add the dataset file to the project folder.")
