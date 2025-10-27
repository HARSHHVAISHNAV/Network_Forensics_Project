import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import numpy as np
import os
import joblib

# -------------------------------
# Step 1: Load Dataset
# -------------------------------
print("Loading dataset...")
data = pd.read_csv("data/dataset.csv")  

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)
print("Columns:", data.columns[:10], "...")  # print first 10 columns

# -------------------------------
# Step 2: Preprocess the Data
# -------------------------------
print("\nCleaning and encoding data...")

# Convert categorical columns to numeric
for col in data.columns:
    if data[col].dtype == 'object':
        data[col] = pd.factorize(data[col])[0]

# Separate features (X) and target (y)
X = data.drop(columns=['label'])
y = data['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Data ready for model training!")

# -------------------------------
# Step 3: Train the Model
# -------------------------------
print("\nTraining Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model training complete!")

# -------------------------------
# Step 4: Evaluate the Model
# -------------------------------
print("\nEvaluating model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -------------------------------
# Step 5: Visualize Distribution
# -------------------------------
unique, counts = np.unique(y, return_counts=True)
plt.bar(unique, counts)
plt.title("Normal vs Attack Distribution")
plt.xlabel("Class Label")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -------------------------------
# Step 6: Generate Forensic Report
# -------------------------------
print("\nGenerating forensic report...")
os.makedirs("forensic_report", exist_ok=True)

with open("forensic_report/report.txt", "w") as f:
    f.write("=== Network Forensics Report ===\n\n")
    f.write(f"Total Records: {len(data)}\n")
    f.write(f"Model Accuracy: {accuracy * 100:.2f}%\n\n")
    f.write("Attack Distribution:\n")
    for val, cnt in zip(unique, counts):
        f.write(f"  {val}: {cnt}\n")
    f.write("\nModel Summary:\n")
    f.write(classification_report(y_test, y_pred))

print("Forensic report generated: forensic_report/report.txt")

# -------------------------------
# Step 7: Save Model
# -------------------------------
joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")

# -------------------------------
# Step 8: Save Feature Columns
# -------------------------------
feature_columns = X.columns
joblib.dump(feature_columns, "feature_columns.pkl")
print("Saved feature column names as feature_columns.pkl")