


def generate_validation(df):
 validation={}

 validation["missing_values","missing_values_percentage"]=missing_values(df)
 validation["duplicate_rows","duplicate_rows_percentage"]=duplicate_rows(df)
 validation["outliers"]=outliers(df)
 validation["data_types"]=df.dtypes.astype(str).to_dict()




 def missing_values(df):
        missing_values = df.isnull().sum()
        missing_values_percentage= (missing_values / len(df)) * 100
        return missing_values, missing_values_percentage
 
 def duplicate_rows(df):
        duplicate_rows = df.duplicated().sum()
        duplicate_rows_percentage = (duplicate_rows / len(df)) * 100
        return duplicate_rows, duplicate_rows_percentage
 
 def outliers(df):
        outliers = {}
        for column in df.select_dtypes(include=['float64', 'int64']).columns:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers[column] = df[(df[column] < lower_bound) | (df[column] > upper_bound)].shape[0]
        return outliers

def data_types(df):
     data_types = df.dtypes.astype(str).to_dict()
     return data_types