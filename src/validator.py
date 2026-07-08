import pandas as pd

def validate_data(clean_df):
    working_df=clean_df.copy()
    working_df["validation_errors"]=pd.NA
    return working_df
