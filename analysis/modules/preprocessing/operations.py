import pandas as pd
from sklearn.preprocessing import LabelEncoder


OPERATIONS = {

    "Missing Values": [
        "Mean",
        "Median",
        "Mode",
        "Drop Rows"
    ],

    "Encoding": [
        "One Hot",
        "Label",
        "Ordinal",
        "Frequency"
    ],

    "Scaling": [
        "Standard",
        "MinMax",
        "Robust",
        "MaxAbs"
    ],

    "Outliers": [
        "Remove",
        "Cap",
        "Winsorize"
    ],

    "Duplicates": [
        "Remove"
    ],

    "Feature Selection": [
        "Drop Column"
    ],

    "Datatype": [
        "String",
        "Integer",
        "Float",
        "Datetime"
    ]
}

#missing value operations

def fill_missing(df,column,method):

    processed_df = df.copy()

    #mean
    if method == "Mean":

        processed_df[column]=processed_df[column].fillna(
            processed_df[column].mean()
        )
    #median
    elif method == "Median":
        processed_df[column]=processed_df[column].fillna(processed_df[column].median())
    #mode
    elif method == "Mode":

        mode=processed_df[column].mode()

        if not mode.empty:
            processed_df[column]=processed_df[column].fillna(mode.iloc[0])
    elif method == "Drop Rows":
        

        processed_df=processed_df.dropna(subset=[column])
    return processed_df                  
def one_hot_encode(df,column):
    processed_df=df.copy()

    processed_df=pd.get_dummies(processed_df,columns=[column],dtype=int)

    return processed_df
def label_encode(df,column):
    processed_df=df.copy()
    encoder=LabelEncoder()
    processed_df[column]=encoder.fit_transform(processed_df[column].astype(str))
    return processed_df
def ordinal_encode(df,column):
    processed_df=df.copy()
    categories=sorted(processed_df[column].dropna().unique())
    mapping={
        category : index
        for index,category in enumerate(categories)
    }
    processed_df[column]=(processed_df[column].map(mapping))
    return processed_df
def frequency_encode(df,column):
    processed_df=df.copy()
    frequency=(processed_df[column].value_counts())
    processed_df[column]=(processed_df[column].map(frequency))
    return processed_df