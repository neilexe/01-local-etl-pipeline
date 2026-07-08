import pandas as pd

def validate_data(clean_df):
    working_df=clean_df.copy()
    working_df["validation_errors"]=pd.NA
    missing_customer_id=working_df["customer_id"].isna()
    working_df.loc[missing_customer_id,"validation_errors"]="Customer ID is missing"
    return working_df
