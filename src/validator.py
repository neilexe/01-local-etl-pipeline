import pandas as pd
from src.utils import append_error

def validate_data(clean_df):
    working_df=clean_df.copy()
    working_df["validation_errors"]=pd.NA
    missing_customer_id=working_df["customer_id"].isna()
    # working_df.loc[missing_customer_id,"validation_errors"]="Customer ID is missing"
    working_df.loc[missing_customer_id,"validation_errors"]=(
        working_df.loc[missing_customer_id,"validation_errors"].apply(
            lambda error : append_error(error, "Customer ID is missing")
        )
    )
    return working_df
