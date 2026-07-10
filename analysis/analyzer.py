
from analysis.component.dataset_summary import generate_summary
def analyze_dataset(df):
    analysis_report = {}
    analysis_report["summary"] = generate_summary(df)
    return analysis_report