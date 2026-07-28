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

if "pipeline" not in st.session_state:
    st.session_state.pipeline = Pipeline()

st.title("🛠 Data Preprocessing Studio")

st.divider()

left, center, right = st.columns([1, 2, 2])

with left:
    render_operation_panel()

with center:
    render_configuration_panel()

with right:
    render_pipeline_panel()

st.divider()

st.button(
    "▶ Run Pipeline",
    type="primary",
    use_container_width=True
)