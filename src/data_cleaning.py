
import pandas as pd

# Function 1 (Copilot-assisted)

def load_data(file_path: str):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None

# Function 2 (Copilot-assisted):

def clean_column_names(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

# Strip whitespace from text columns

def strip_whitespace(df):
    text_cols = ["prodname", "category"]

    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    return df

# Handle missing prices and quantities

def handle_missing_values(df):
    df = df.dropna(subset=["price", "qty"])
    return df

# Remove invalid rows (negative price or quantity)

def remove_invalid_rows(df):
    df = df[(df["price"] >= 0) & (df["qty"] > 0)]
    return df

# MAIN EXECUTION BLOCK

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)

    if df_raw is not None:
        df_clean = clean_column_names(df_raw)
        df_clean = strip_whitespace(df_clean)
        df_clean = handle_missing_values(df_clean)
        df_clean = remove_invalid_rows(df_clean)

        df_clean.to_csv(cleaned_path, index=False)

        print("Cleaning complete. First few rows:")
        print(df_clean.head())
