

def generate_statistics(df):
    statistics = {}
    statistics["mean"] = mean(df)
    statistics["median"] = median(df)
    statistics["mode"] = mode(df)
    statistics["std_dev"] = std_dev(df)
    statistics["maximum"] = df.max(numeric_only=True)
    statistics["minimum"] = df.min(numeric_only=True)
    statistics["25th_percentile"] = df.quantile(0.25, numeric_only=True)
    statistics["75th_percentile"] = df.quantile(0.75, numeric_only=True)
    statistics["variance"] = df.var(numeric_only=True)
    statistics["skewness"] = df.skew(numeric_only=True)
    statistics["kurtosis"] = df.kurt(numeric_only=True)
    statistics["correlation_matrix"] = df.corr(numeric_only=True)
    statistics["covariance_matrix"] = df.cov(numeric_only=True)
    statistics["unique_values"] = df.nunique()
    statistics["most_frequent_values"] = df.mode(numeric_only=True).iloc[0] if not df.mode(numeric_only=True).empty else None
    statistics["missing_values"] = df.isnull().sum()

    return statistics


 
def mean(df):
    mean_values = df.mean(numeric_only=True)
    return mean_values
def median(df):
    median_values = df.median(numeric_only=True)
    return median_values
def mode(df):
    mode_values = df.mode(numeric_only=True).iloc[0] if not df.mode(numeric_only=True).empty else None
    return mode_values
def std_dev(df):
    std_dev_values = df.std(numeric_only=True)
    return std_dev_values
