# import the material like a carpenter collect the tools that they use in building anything
import streamlit as st
import pandas as pd

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

#read the file and display the data
    df=pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df)
