from config.settings import RAW_CUSTOMER_FILE
from src.reader import read_raw_data
from src.cleaner import clean_data
from src.validator import validate_data


def main():
    """
    Orchestrates the Local ETL Pipeline.
    """
    raw_df=read_raw_data(RAW_CUSTOMER_FILE)
    clean_df=clean_data(raw_df)
    validated_df=validate_data(clean_df)
    print(validated_df)

if __name__ == "__main__":
    main()