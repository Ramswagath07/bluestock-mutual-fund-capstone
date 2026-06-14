import pandas as pd
from pathlib import Path

# Path to raw data folder
RAW_DATA_PATH = Path("data/raw")

def inspect_csv(file_path):
    print("\n" + "=" * 60)
    print(f"FILE: {file_path.name}")
    print("=" * 60)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file_path.name}: {e}")

def main():
    csv_files = list(RAW_DATA_PATH.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in data/raw folder.")
        return

    for file in csv_files:
        inspect_csv(file)

if __name__ == "__main__":
    main()