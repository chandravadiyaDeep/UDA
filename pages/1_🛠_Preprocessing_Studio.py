import streamlit as st

st.set_page_config(
    page_title="Preprocessing Studio",
    page_icon="🛠",
    layout="wide"
)

st.title("🛠 Data Preprocessing Studio")

st.divider()

#dataset information
col1,col2 =st.columns(2)

with col1:
    st.metric("Dataset","No Dataset")
with col2:
    st.metric("Pipeline Steps","0")

st.divider()

#main layout
left, center , right=st.columns([1,2,1])
#left panel
with left:
    st.subheader("⚙ Operations")

    st.button("Missing Values",use_container_width=True)

    st.button("Encoding",use_container_width=True)

    st.button("Scaling",use_container_width=True)

    st.button("Outliers",use_container_width=True)

    st.button("Duplicates",use_container_width=True)

    st.button("Features Selection",use_conatiner_width=True)

    st.button("Data Type",use_conatainer_width=True)

