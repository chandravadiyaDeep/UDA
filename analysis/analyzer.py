
from analysis.component.dataset_summary import generate_summary
from analysis.component.dataset_validator import generate_validation
def analyze_dataset(df):
    analysis_report = {}
    analysis_report["summary"] = generate_summary(df)
    analysis_report["validation"] = generate_validation(df)
    return analysis_report