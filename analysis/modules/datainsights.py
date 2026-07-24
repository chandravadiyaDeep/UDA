


def generate_data_insights(analysis_report,df):
    summary = analysis_report["summary"]
    validation = analysis_report["validation"]
    statistics = analysis_report["statistics"]
    insights = {}

    insights["datatype"]=datatype_insights(summary)
    insights["feature_detection"]=feature_detection(df,summary,validation,statistics)
    insights["ml_readness"]=ml_readiness(df,summary,validation,statistics)
    insights["quality_score"]=quality_score(df, summary, validation, statistics)

    return insights
        
def datatype_insights(summary):
    insights=[]

    data_types=summary["data_types"]
    total_columns=summary["columns"]

    numerical = 0
    categorical = 0
    boolean = 0
    datetime = 0

    for dtype in data_types.values():

        dtype = dtype.lower()

        #numerical
        if dtype in [
            "int64",
            "int32",
            "int16",
            "int8",
            "float64",
            "float32",
            "float16"
            ]:
            numerical += 1
         #boolean
        elif dtype == "bool":
            boolean+=1

         #datetime
        elif "datetime" in dtype:
            datetime+=1

          #evrything else -> categorical
        else:
            categorical +=1


    numerical_percent = round((numerical / total_columns)*100,1)  
    categorical_percent=round((categorical/total_columns)*100,1)

    #insights

    insights.append(
        f"✅{numerical_percent}% of the features are numerical."
    )
    insights.append(
        f"✅{categorical_percent}% of the features are categorical."
    )

    #mixed datasets
    if numerical > 0 and categorical > 0:
        insights.append(
            "💡 Datasets contains both numerical and categorical features."
        )
    #mostly numerical
    if numerical_percent >= 70:
        insights.append(
            "💡 Most features are numerical."
        )
     #boolean
    if boolean > 0:
        insights.append(
            f"💡 Dataset contains {boolean} boolean feature(s)."
        )
    if datetime > 0:
        insights.append(
            f"💡 Dataset contains {datetime} datetime feature(s)."
        )          
    return insights
def feature_detection(df,summary):
    insights=[]

    total_rows=summary["rows"]
    data_types=summary["data_types"]

    for column in df.columns:

        dtype=data_types[column].lower()

        unique_count=df[column].nunique(dropna=True)

        column_lower=column.lower()

        #id detection
        if(
            "id" in column_lower
            and unique_count >= total_rows*0.95
        ):
            insights.append(
                f"💡 '{column}' appears to be an identifier column."
            )

       #constant column
        if unique_count==1:
            insights.append(
                    f"💡 '{column}' contains only one unique value."     
                )

        #binary features
        if unique_count == 2:
            insights.append(
                    f"💡 '{column}' is a binary feature."           
                )
       #low cardinality
        if(
            dtype == "object"
            and 2 < unique_count <=10
            ):
            insights.append(
                f"💡 '{column}' has low cardinality ({unique_count} unique values)."           
                )
        #high cardanlity
        if(
                dtype== "object"
                and unique_count > total_rows*0.5
            ):
                insights.append(
                    f"💡 '{column}' has high cardinality."   
                )
        #datetime features
        if "datetime" in dtype:
                insights.append(
                    f"💡 '{column}' is a datetime feature."
                )
    return insights

def ml_readiness(df,summary,validation):
    insights=[]

    total_rows=summary["rows"]
    data_types=summary["data_types"]

    #missing values recommendation
    missing_values=validation.get("missing_values",{})

    for column, percentage in missing_values.items():

        if percentage > 0:
            insights.append(
                f"🤖 '{column}' requires missing value imputation before model training."
            )

    #encoding recommendation
    for column, dtype in data_types.items():

        dtype = dtype.lower()

        if dtype == "object":
            insights.append(
                f"🤖'{column}' requires categorical encoding."
            )

    #high cardinality
    for column in df.columns:

        unique_count=df[column].nunique(dropna=True)

        if (
            data_types[column].lower() == "object"
            and unique_count > total_rows *0.5
        ):
            insights.append(
                f"🤖'{column}' may benefit from target or frequency encoding."
            )
    #contant columns
    for column in df.columns:

        if df[column].nunique(dropna=True) == 1:

            insights.append(
                f"🤖'{column}' has zero variance and can be removed."
            )         
    #Datetime features
    for column,dtype in data_types.items():

        if "datetime" in dtype.lower():

            insights.append(
                f"🤖 Consider extracting Year,Month, Day or weekday from '{column}'."
            )

    return insights          
def quality_score(df, summary, validation):

    score = 100
    reasons = []

    total_rows = summary["rows"]
    data_types = summary["data_types"]

    # ---------------------------------------
    # Missing Values
    # ---------------------------------------
    missing_values = validation.get("missing_values", {})

    for column, percentage in missing_values.items():

        if percentage > 0 and percentage <= 10:
            score -= 2
            reasons.append(f"{column}: Minor missing values (-2)")

        elif percentage > 10 and percentage <= 30:
            score -= 5
            reasons.append(f"{column}: Moderate missing values (-5)")

        elif percentage > 30:
            score -= 10
            reasons.append(f"{column}: High missing values (-10)")

    # ---------------------------------------
    # Duplicate Rows
    # ---------------------------------------
    duplicate_rows = validation.get("duplicate_rows", 0)

    if duplicate_rows > 0:
        score -= 5
        reasons.append("Duplicate rows detected (-5)")

    # ---------------------------------------
    # Constant Columns
    # ---------------------------------------
    for column in df.columns:

        if df[column].nunique(dropna=True) == 1:

            score -= 4

            reasons.append(
                f"{column}: Constant feature (-4)"
            )

    # ---------------------------------------
    # High Cardinality
    # ---------------------------------------
    for column in df.columns:

        unique_count = df[column].nunique(dropna=True)

        if (
            data_types[column].lower() == "object"
            and unique_count > total_rows * 0.5
        ):

            score -= 2

            reasons.append(
                f"{column}: High cardinality (-2)"
            )

    # ---------------------------------------
    # Score Limits
    # ---------------------------------------
    score = max(0, min(100, score))

    # ---------------------------------------
    # Rating
    # ---------------------------------------
    if score >= 90:
        rating = "Excellent"

    elif score >= 75:
        rating = "Good"

    elif score >= 60:
        rating = "Fair"

    elif score >= 40:
        rating = "Poor"

    else:
        rating = "Very Poor"

    return {
        "score": score,
        "rating": rating,
        "reasons": reasons
    }