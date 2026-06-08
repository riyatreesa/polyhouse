import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Summary statistics
print("SUMMARY STATISTICS")
print(df.describe())

# Rule violations
print("\nRULE VIOLATIONS")
print("Temperature < 0:", (df["temperature"] < 0).sum())
print("Humidity > 100:", (df["humidity"] > 100).sum())
print("CO2 < 0:", (df["co2"] < 0).sum())
print("Yield < 0:", (df["yield"] < 0).sum())

# Correlation Heatmap
corr = df[["temperature", "humidity", "co2", "yield"]].corr()

plt.figure(figsize=(6, 4))
plt.imshow(corr, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.savefig("reports/figures/correlation_heatmap.png")
plt.close()

# Humidity vs Yield
plt.figure(figsize=(6, 4))
plt.scatter(df["humidity"], df["yield"])
plt.xlabel("Humidity (%)")
plt.ylabel("Yield (kg)")
plt.title("Humidity vs Yield")
plt.savefig("reports/figures/humidity_vs_yield.png")
plt.close()

# CO2 vs Yield
plt.figure(figsize=(6, 4))
plt.scatter(df["co2"], df["yield"])
plt.xlabel("CO2")
plt.ylabel("Yield (kg)")
plt.title("CO2 vs Yield")
plt.savefig("reports/figures/co2_vs_yield.png")
plt.close()

print("\nEDA COMPLETE")
print("Figures saved in reports/figures/")