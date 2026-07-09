import pandas as pd
from config.settings import LOCAL_STORAGE_PATH

def export_to_local(validated_df):
    validated_df.to_csv(LOCAL_STORAGE_PATH, index = False)
    
    

        