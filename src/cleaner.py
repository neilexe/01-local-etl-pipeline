'''
Receives a raw customer DataFrame.

Performs generic data cleaning operations that do not require business knowledge.

Returns a cleaned DataFrame while preserving the original input.
'''
import pandas as pd
from src.reader import read_raw_data


def clean_data(raw_df):
    working_df=raw_df.copy()
    
    working_df=working_df.loc[:, ~working_df.columns.str.contains("^Unnamed")]
    
    for column in working_df.columns:
        if working_df[column].dtype == "str":
            working_df[column]=working_df[column].str.strip()


    return working_df

# if __name__ == "__main__":
#     file_path="/Users/neilbanerjee/Documents/Python Course/Pandas Practice/today_customers.csv"
#     raw_df=read_raw_data(file_path)
#     print(raw_df.head())
#     clean_data(raw_df)