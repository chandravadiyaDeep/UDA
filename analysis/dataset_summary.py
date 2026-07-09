def generate_summary(df):
    summary = {}
    summary["rows"] = df.shape[0]
    summary["columns"] = df.shape[1]
    return summary
    