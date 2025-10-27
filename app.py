import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load trained model and label mapping
model = joblib.load("model.pkl")
label_mapping = pd.read_csv("label_mapping.csv")

st.set_page_config(page_title="Network Traffic Analyzer",layout="wide")

st.title("Network Traffic Analyzer")
st.markdown("Upload network traffic data and let the system detect possible intrusions or anomalies.")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data Preview")
    st.dataframe(df.head())

    # Predict
    st.write("### Predicting...")

    # Load the feature columns used during training
    feature_columns = joblib.load("feature_columns.pkl")

    # Ensure 'label' or other unwanted columns are not included
    if "label" in df.columns:
        df = df.drop(columns=["label"])

    # Convert categorical columns to numeric (same as training)
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = pd.factorize(df[col])[0]

    # Align test data with training features
    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0  
    df = df[feature_columns]  

    # Predict using the trained model
    predictions = model.predict(df)

    # Add predictions to the dataframe
    df["Predicted_Label"] = predictions

    # Map label numbers to attack names if possible
    if "label" in label_mapping.columns:
        mapping_dict = label_mapping.set_index("label").to_dict().get("label", {})
        df["Predicted_Name"] = df["Predicted_Label"].map(mapping_dict)

    st.write("### Prediction Results")
    st.dataframe(df.head())

    # Summary counts
    counts = df["Predicted_Label"].value_counts()

    st.write("### Traffic Distribution")
    fig, ax = plt.subplots()
    counts.plot(kind="bar", ax=ax)
    ax.set_xlabel("Attack Label")
    ax.set_ylabel("Count")
    st.pyplot(fig)

else:
    st.info("Please upload a CSV file to start analysis.")
