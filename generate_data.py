import pandas as pd

rows = []

for i in range(1, 61):
    rows.append({
        "temperature": round(28 + i * 0.25, 2),
        "humidity": round(70 + i * 0.8, 1),
        "co2": 650 + i * 8,
        "yield": round(12 + i * 0.15, 2)
    })

df = pd.DataFrame(rows)

# Add some missing values
df.loc[5, "temperature"] = None
df.loc[10, "humidity"] = None
df.loc[15, "co2"] = None
df.loc[20, "yield"] = None

df.to_csv("data/raw/polyhouse_sensor.csv", index=False)

print("Rows:", len(df))