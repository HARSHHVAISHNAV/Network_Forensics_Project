import pandas as pd

# Load the dataset
df = pd.read_csv("data/dataset.csv")

# Show sample rows to check structure
print(df.head())

# Check if both label name and numeric columns exist
if 'label' not in df.columns:
    raise ValueError("No 'label' column found!")
    
# Find the unique combinations of attack names and labels
mapping = df[['label']].drop_duplicates().reset_index(drop=True)

print("\nUnique label mappings found:")
print(mapping)

# Save mapping to a CSV file
mapping.to_csv("label_mapping.csv", index=False)
print("\nLabel mapping saved as label_mapping.csv")
