import pandas as pd
import os

def clean_sales_data():
    # File paths
    raw_path = "data/raw/sales_data_raw.csv"
    processed_path = "data/processed/sales_data_cleaned.csv"

    # Load raw data
    df = pd.read_csv(raw_path)

    # 1 Remove duplicate rows
    df = df.drop_duplicates()

    #  Strip extra whitespace from column names
    df.columns = df.columns.str.strip()

    # Strip whitespace in string columns
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # Convert date column if it exists
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Fill missing numeric values with 0
    num_cols = df.select_dtypes(include=["number"]).columns
    df[num_cols] = df[num_cols].fillna(0)

    # Fill missing text values with "Unknown"
    text_cols = df.select_dtypes(include=["object"]).columns
    df[text_cols] = df[text_cols].fillna("Unknown")

    # Make sure processed folder exists
    os.makedirs("data/processed", exist_ok=True)

    # Save cleaned data
    df.to_csv(processed_path, index=False)

    print("Data cleaned and saved to:", processed_path)


if __name__ == "__main__":
    clean_sales_data()
