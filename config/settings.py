from pathlib import Path

RAW_CUSTOMER_FILE='/Users/neilbanerjee/Documents/Python Course/Pandas Practice/today_customers_2.csv'
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIRECTORY = PROJECT_ROOT / "output"
LOCAL_STORAGE_PATH = OUTPUT_DIRECTORY / "output.csv"
OUTPUT_DIRECTORY.mkdir(exist_ok=True)