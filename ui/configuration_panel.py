import streamlit as st


def render_configuration_panel(df):
    #column divider for different category
    all_columns=df.columns.tolist()
    numeric_columns=df.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns=df.select_dtypes(include=["object","category"]).columns.tolist()


    operation = st.session_state.get("current_operation")

    st.subheader("⚙ Configuration")

    if operation is None:

        st.info("Select an operation.")

        return

    st.write(f"Current Operation : **{operation}**")

    if operation == "Missing Values":
        column = st.selectbox("Column",all_columns)

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
    elif operation == "encoding":

    column = st.selectbox(
        "Column",
        categorical_columns
    )

    method = st.selectbox(
        "Method",
        [
            "One Hot",
            "Label",
            "Ordinal",
            "Frequency"
        ]
    )

    if st.button(
        "Add Step",
        use_container_width=True
    ):

        st.session_state.pipeline.add_step(

            category="Encoding",

            column=column,

            method=method

        )

        st.success("Step Added Successfully")         