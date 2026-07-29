from analysis.modules.preprocessing.operations import fill_missing

def execute_pipeline(df, pipeline):
    processed_df=df.copy()
    #get all the pipeline steps
    steps=pipeline.get_steps()

    for step in steps:
        category=step["category"]

        #missing value
        if category == "Missing Values":
            processed_df=fill_missing(processed_df,column=step["column"],method=step["method"])

    return processed_df        
