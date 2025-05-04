import streamlit as st
import pandas as pd
import joblib

# Load the models
abc_model = joblib.load("abc_classifier.pkl")
xyz_model = joblib.load("xyz_classifier.pkl")

st.title("Inventory Classification App")

uploaded_file = st.file_uploader("Upload your inventory CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data", df)

    # Preprocess for prediction (drop non-numeric, etc.)
    features = df.select_dtypes(include='number')

    # Predict
    abc_preds = abc_model.predict(features)
    xyz_preds = xyz_model.predict(features)

    # Show results
    df["ABC_Prediction"] = abc_preds
    df["XYZ_Prediction"] = xyz_preds

    st.write("### Predictions", df[["ABC_Prediction", "XYZ_Prediction"]])
