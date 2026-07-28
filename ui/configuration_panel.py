import streamlit as st


def render_configuration_panel():

    operation = st.session_state.get("current_operation")

    st.subheader("⚙ Configuration")

    if operation is None:

        st.info("Select an operation.")

        return

    st.write(f"Current Operation : **{operation}**")

    if operation == "Missing Values":

        column = st.selectbox(
            "Column",
            [
                "Age",
                "Fare",
                "Cabin"
            ]
        )

        method = st.selectbox(
            "Method",
            [
                "Mean",
                "Median",
                "Mode",
                "Drop Rows"
            ]
        )

        if st.button("Add Step", use_container_width=True):

            st.session_state.pipeline.add_step(

                category="Missing Values",

                column=column,

                method=method
            )

            st.success("Step Added Successfully")