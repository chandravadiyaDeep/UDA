import streamlit as st


def render_pipeline_panel():

    st.subheader("🧩 Pipeline")

    steps = st.session_state.pipeline.get_steps()

    if len(steps) == 0:

        st.info("No preprocessing steps added.")

        return

    for index, step in enumerate(steps, start=1):

        st.success(

            f"{index}. {step['category']} → {step['column']} ({step['method']})"

        )