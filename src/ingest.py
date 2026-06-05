from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")

def load_data():
    files = list(RAW_DIR.glob("*.csv"))

    if not files:
        raise FileNotFoundError("No CSV files found")

    dfs = []

    for file in files:
        df = pd.read_csv(file)
        df["source_file"] = file.name
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)

if __name__ == "__main__":
    df = load_data()

    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())