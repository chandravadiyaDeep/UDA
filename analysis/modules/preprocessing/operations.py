import pandas as pd


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

    processed_df = df.copy

    #mean
    if method == "mean":

        processed_df[column]=processed_df[column].fillna(
            processed_df[column].mean
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
