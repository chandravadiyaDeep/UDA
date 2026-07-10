# import the material like a carpenter collect the tools that they use in building anything
import streamlit as st
import pandas as pd
# connecting the function
from analysis.analyzer import analyze_dataset

#configuthe the page
st.set_page_config(page_title="Universal Data Analyzer")

#title of the page
st.title("📊 Universal Data Analyzer")

#description
st.write("upload your data file and begin the analysis.")

#file uploader
# this upload_file is the variable bridge between ui and data engine
uploaded_file=st.file_uploader("Choose a CSV file",type=["csv"])

#user validation
if uploaded_file is not None:

    st.success("File uploaded successfully!")
        
    df=pd.read_csv(uploaded_file) 

    st.subheader("Dataset preview:")

    st.dataframe(df.head(5))
    
    analysis_report=analyze_dataset(df)

    st.subheader("Dataset Summary:")

    summary=analysis_report["summary"]

    st.write("Rows:",summary["rows"])
    st.write("Columns:",summary["columns"])
    st.write("Shape:",summary["shape"])
    st.write("Column Names:",summary["column_names"])
    st.write("Data Types:",summary["data_types"])
