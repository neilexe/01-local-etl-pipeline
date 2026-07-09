import pandas as pd

def generate_report(validated_df):
    failed_rows=validated_df[validated_df["validation_errors"].notna()]
    return failed_rows