
from analysis.component.dataset_summary import generate_summary
from analysis.component.dataset_validator import generate_validation
from analysis.component.dataset_statistics import generate_statistics
from modules import generate_data_insights
def analyze_dataset(df):
    analysis_report = {}
    analysis_report["summary"] = generate_summary(df)
    analysis_report["validation"] = generate_validation(df)
    analysis_report["statistics"] = generate_statistics(df)
    analysis_report["data_insights"] = generate_data_insights(df)
    return analysis_report