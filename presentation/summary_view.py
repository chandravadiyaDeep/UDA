import streamlit as st

st.subheader("📋 Dataset Summary")

def render_summary(summary):
    st.write("**Number of Rows:**", summary["rows"])
    st.write("**Number of Columns:**", summary["columns"])
    st.write("**Shape:**", summary["shape"])
    st.write("**Column Names:**", summary["column_names"])
    st.write("**Data Types:**", summary["data_types"])
    st.write("**Memory Usage (bytes):**", summary["memory_usage"])