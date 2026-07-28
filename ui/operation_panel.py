import streamlit as st

def render_operation_panel():

    st.subheader("⚙ Operations")

    operations=[
        "Missing Values",
        "Encoding",
        "Scaling",
        "Outliers",
        "Duplicates",
        "Feature Selection",
        "Data Type"
    ]

    for operation in operations:

        if st.button(operation, use_container_width=True):

            st.session_state.current_operation = operation