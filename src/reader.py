import pandas as pd
'''
Reads the Vendor CSV file and returns a Pandas DataFrame
'''
def read_raw_data(file_path):
    try:
        return pd.read_csv(file_path)
    
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Input file not not found.\n"
            f"Expected location:\n"
            f"{file_path}\n"
            f"Pipeline aborted."
        )