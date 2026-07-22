


def generate_data_insights(analysis_report):
    summary = analysis_report["summary"]
    validation = analysis_report["validation"]
    statistics = analysis_report["statistics"]
    insights = {}

    insights["datatype"]=datatype_insights(summary)

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
            "float64",
            "int32",
            "float32",
            "int16",
            "float16",
            "int8",
            "float8",
        ]:
            numerrical += 1
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
        f"✅{categorical_percent}% of the features are numerical."
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

    
