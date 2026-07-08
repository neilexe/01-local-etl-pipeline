import pandas as pd

def append_error(current_error, new_error):
    if pd.isna(current_error):
        return new_error
    else:
        return f"{current_error} | {new_error}"
