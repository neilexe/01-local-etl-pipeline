import pandas as pd
from src.utils import append_error

def validate_data(clean_df):
    working_df = clean_df.copy()
    working_df["validation_errors"] = pd.NA
    missing_customer_id = working_df["customer_id"].isna()
    duplicate_customer_id = working_df["customer_id"].duplicated(keep=False)
    negative_age = working_df["age"] < 0
    negative_salary = working_df["salary"] < 0

    # working_df.loc[missing_customer_id,"validation_errors"]="Customer ID is missing"
    working_df.loc[missing_customer_id,"validation_errors"] = (
        working_df.loc[missing_customer_id,"validation_errors"].apply(
            lambda error : append_error(error, "Customer ID is missing")
        )
    )

    working_df.loc[duplicate_customer_id, "validation_errors"] = (
        working_df.loc[duplicate_customer_id, "validation_errors"].apply(
            lambda error : append_error(error, "Duplicate Customer ID")
        )
    )

    working_df.loc[negative_age, "validation_errors"] = (
        working_df.loc[negative_age, "validation_errors"].apply(
            lambda error : append_error(error, "Age cannot be negative")
        )
    )

    working_df.loc[negative_salary, "validation_errors"] = (
        working_df.loc[negative_salary, "validation_errors"].apply(
            lambda error : append_error(error, "Salary cannot be")
        )
    )


    return working_df
