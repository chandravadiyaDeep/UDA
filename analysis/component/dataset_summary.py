

def _get_memory_usage(df):
    memory = df.memory_usage(deep=True).sum()
    return memory

def generate_summary(df):
    summary = {}
    summary["rows"] = df.shape[0]
    summary["columns"] = df.shape[1]
    summary["shape"]=df.shape
    summary["column_names"]=list(df.columns)
    summary["data_types"] = df.dtypes.astype(str).to_dict()
    summary["memory_usage"] = _get_memory_usage(df)
    return summary

def _get_memory_usage(df):
    memory = df.memory_usage(deep=True).sum()
    return memory