# Import the required libraries
import streamlit as st
import pandas as pd

# Connect the analysis function
from analysis.analyzer import analyze_dataset

# Configure the page
st.set_page_config(page_title="Universal Data Analyzer")

# Title
st.title("📊 Universal Data Analyzer")

# Description
st.write("Upload your data file and begin the analysis.")

# ==========================
# Stage 1 : Upload Dataset
# ==========================

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

# If user uploads a new dataset
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # Store dataset in Session State
    st.session_state.df = df


# ==========================
# Stage 2 : Check Dataset
# ==========================

if "df" not in st.session_state:

    st.info("Please upload a CSV file to begin.")

    st.stop()


# ==========================
# Stage 3 : Use Session Data
# ==========================

df = st.session_state.df

# Success Message
st.success("Dataset Loaded Successfully ✅")

# Dataset Preview
st.subheader("📄 Dataset Preview")

st.dataframe(df.head(5))

# Analyze Dataset
analysis_report = analyze_dataset(df)

# ==========================
# Dataset Summary
# ==========================

st.subheader("📋 Dataset Summary")

st.json(analysis_report["summary"])

# ==========================
# Dataset Validation
# ==========================

st.subheader("✅ Dataset Validation")

st.json(analysis_report["validation"])

# ==========================
# Dataset Statistics
# ==========================

st.subheader("📈 Dataset Statistics")

st.json(analysis_report["statistics"])

# ==========================
# Dataset Insights
# ==========================

st.subheader("💡 Dataset Insights")

st.json(analysis_report["data_insights"])