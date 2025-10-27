import pandas as pd

# Load the dataset
df = pd.read_csv("data/dataset.csv")

# Show basic info
print("Columns:", df.columns.tolist())

# Display first few rows
print("\nSample rows:\n", df.head())

# Check what unique labels exist
if 'label' in df.columns:
    print("\nUnique values in label column:\n", df['label'].unique())
else:
    print("\nNo column named 'label' found. Please check the correct column name.")
