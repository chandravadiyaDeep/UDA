def missing_value(df):
    return df.isnull().sum()


def missing_percentage(df):
    return (df.isnull().sum() / len(df)) * 100


def duplicate_row(df):
    return df.duplicated().sum()


def duplicate_row_percentage(df):
    return (df.duplicated().sum() / len(df)) * 100


def outlier(df):
    outliers = {}

    for column in df.select_dtypes(include=["float64", "int64"]).columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers[column] = df[
            (df[column] < lower_bound) | (df[column] > upper_bound)
        ].shape[0]

    return outliers


def data_type(df):
    return df.dtypes.astype(str).to_dict()


def generate_validation(df):
    validation = {}

    validation["missing_values"] = missing_value(df)
    validation["missing_values_percentage"] = missing_percentage(df)
    validation["duplicate_rows"] = duplicate_row(df)
    validation["duplicate_rows_percentage"] = duplicate_row_percentage(df)
    validation["outliers"] = outlier(df)
    validation["data_types"] = data_type(df)

    return validation