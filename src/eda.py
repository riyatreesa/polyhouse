import os
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Create figures folder
os.makedirs("reports/figures", exist_ok=True)

# -----------------------
# Correlation Heatmap
# -----------------------
features = ["temperature", "humidity", "co2", "yield"]

fig, ax = plt.subplots(figsize=(6, 5))

corr_matrix = df[features].corr()

im = ax.imshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)

ax.set_xticks(range(len(features)))
ax.set_xticklabels(features, rotation=45)

ax.set_yticks(range(len(features)))
ax.set_yticklabels(features)

fig.colorbar(im, ax=ax, label="Pearson r")

ax.set_title("Sensor & Yield Correlations")

plt.tight_layout()
plt.savefig("reports/figures/corr_heatmap.png")
plt.close()

# -----------------------
# Scatter Plots
# -----------------------
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# Humidity vs Yield
axes[0].scatter(df["humidity"], df["yield"], alpha=0.5)
axes[0].set_title("Humidity vs Yield")
axes[0].set_xlabel("Humidity (%)")
axes[0].set_ylabel("Yield (kg)")

# Temperature vs Yield
axes[1].scatter(df["temperature"], df["yield"], alpha=0.5)
axes[1].set_title("Temperature vs Yield")
axes[1].set_xlabel("Temperature (°C)")
axes[1].set_ylabel("Yield (kg)")

# CO2 vs Yield
axes[2].scatter(df["co2"], df["yield"], alpha=0.5)
axes[2].set_title("CO2 vs Yield")
axes[2].set_xlabel("CO2 (ppm)")
axes[2].set_ylabel("Yield (kg)")

plt.tight_layout()
plt.savefig("reports/figures/scatter_yield.png")
plt.close()

print("EDA complete.")
print("Figures saved in reports/figures/")