def generate_summary(df):
    summary = {}
    summary["rows"] = df.shape[0]
    summary["columns"] = df.shape[1]
    summary["shape"]=df.shape
    summary["column_names"]=list(df.columns)
    summary["data_types"] = df.dtypes.astype(str).to_dict()
    return summary
    