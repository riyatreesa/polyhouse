import pandas as pd

# Show all columns
pd.set_option("display.max_columns", None)

# Show all rows (optional)
pd.set_option("display.max_rows", None)

# Wider terminal display
pd.set_option("display.width", 200)

df = pd.read_parquet("data/processed/02_cleaned.parquet")

print("\nCLEANED DATASET\n")
print(df.to_string(index=False))

print("\nShape:", df.shape)

print("\nNull Counts:")
print(df.isnull().sum())