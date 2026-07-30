from analysis.modules.preprocessing.executor import execute_pipeline    

import streamlit as st

from analysis.modules.preprocessing.pipeline import Pipeline

from ui.operation_panel import render_operation_panel
from ui.configuration_panel import render_configuration_panel
from ui.pipeline_panel import render_pipeline_panel

st.set_page_config(
    page_title="Preprocessing Studio",
    page_icon="🛠",
    layout="wide"
)
if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()
df = st.session_state.df 

if "pipeline" not in st.session_state:
    st.session_state.pipeline = Pipeline()

st.title("🛠 Data Preprocessing Studio")

st.divider()

left, center, right = st.columns([1, 2, 2])

with left:
    render_operation_panel()

with center:
    render_configuration_panel(df)

with right:
    render_pipeline_panel()

st.divider()

if st.button(
    "▶ Run Pipeline",
    type="primary",
    use_container_width=True
):

    processed_df = execute_pipeline(df,st.session_state.pipeline)
    st.session_state.processed_df = processed_df
    st.success("Pipeline executed successfully!")
    
    if "processed_df" in st.session_state:
        st.subheader("Processed Dataset Preview")
        if "processed_df" not in st.session_state or st.session_state.processed_df is None:
            st.warning("Please run the preprocessing pipeline first.")
            st.stop()

        st.write(type(st.session_state.processed_df))
        st.write(st.session_state.processed_df.shape)
        
        st.dataframe(st.session_state.processed_df.head())
        
        csv=st.session_state.processed_df.to_csv(index=False)
        
        st.download_button(
                label="📥 Download Clean Dataset",
                data=csv,
                file_name="cleaned.csv",
                mine="text/csv"
            )
        

    