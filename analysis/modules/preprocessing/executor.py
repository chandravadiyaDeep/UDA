from analysis.modules.preprocessing.operations import (fill_missing,one_hot_encode,label_encode,ordinal_encode,frequency_encode)

def execute_pipeline(df, pipeline):
    processed_df=df.copy()
    #get all the pipeline steps
    steps=pipeline.get_steps()

    for step in steps:
        category=step["category"]

        #missing value
        if category == "Missing Values":
            processed_df=fill_missing(processed_df,column=step["column"],method=step["method"])
        #encoding
        elif category == "Encoding":
            if step["method"] == "One Hot":
                processed_df=one_hot_encode(processed_df,column=step["column"])
            elif step["method"] == "Label":
                processed_df=label_encode(processed_df,column=step["column"])        
            elif step["method"] == "Ordinal":
                processed_df=ordinal_encode(processed_df,column=step["column"])
            elif step["method"] == "Frequency":
                processed_df=frequency_encode(processed_df,column=step["column"])
                      
    return processed_df        
