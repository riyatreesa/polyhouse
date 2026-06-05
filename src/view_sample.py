import pandas as pd

df = pd.read_csv("data/processed/sample_cleaned_50_rows.csv")

df.insert(0, "S.No", range(1, len(df) + 1))

print("TOTAL ROWS:", len(df))
print()

print(df.to_string(index=False))