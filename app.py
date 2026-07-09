# ==========================================================
# Universal Data Analyzer (UDA)
#
# File: app.py
#
# Author : Deep Chandravadiya
# ==========================================================

# Import required library
import streamlit as st

# Configure page
st.set_page_config(
    page_title="Universal Data Analyzer",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Universal Data Analyzer")

# Subtitle
st.write("Upload any CSV file to begin analysis.")

# File uploader
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

# Show status
if uploaded_file is None:
    st.info("Please upload a CSV file.")
else:
    st.success("File uploaded successfully!")