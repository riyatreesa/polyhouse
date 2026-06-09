import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create figures folder
Path("reports/figures").mkdir(parents=True, exist_ok=True)

# Load cleaned dataset
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# -----------------------------------
# Correlation Heatmap
# -----------------------------------
features = ["temperature_c", "humidity_pct", "co2_ppm", "yield_kg"]

corr_matrix = df[features].corr()

# Print correlation matrix
print(corr_matrix)

fig, ax = plt.subplots(figsize=(6, 5))

im = ax.imshow(
    corr_matrix,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

ax.set_xticks(range(len(features)))
ax.set_xticklabels(
    ["temperature", "humidity", "co2", "yield"],
    rotation=45,
    ha="right"
)

ax.set_yticks(range(len(features)))
ax.set_yticklabels(
    ["temperature", "humidity", "co2", "yield"]
)

fig.colorbar(im, ax=ax, label="Pearson r")

ax.set_title("Sensor & Yield Correlations")

plt.tight_layout()

plt.savefig(
    "reports/figures/corr_heatmap.png",
    dpi=150
)

plt.close()

# -----------------------------------
# Combined Scatter Plots
# -----------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Humidity vs Yield
axes[0].scatter(df["humidity_pct"], df["yield_kg"], alpha=0.5, s=20)
axes[0].set_xlabel("Humidity (%)")
axes[0].set_ylabel("Yield (kg)")
axes[0].set_title("Humidity vs Yield")
axes[0].grid(True, alpha=0.3)

# Temperature vs Yield
axes[1].scatter(df["temperature_c"], df["yield_kg"], alpha=0.5, s=20)
axes[1].set_xlabel("Temperature (°C)")
axes[1].set_ylabel("Yield (kg)")
axes[1].set_title("Temperature vs Yield")
axes[1].grid(True, alpha=0.3)

# CO2 vs Yield
axes[2].scatter(df["co2_ppm"], df["yield_kg"], alpha=0.5, s=20)
axes[2].set_xlabel("CO2 (ppm)")
axes[2].set_ylabel("Yield (kg)")
axes[2].set_title("CO2 vs Yield")
axes[2].grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "reports/figures/scatter_plots.png",
    dpi=150
)

plt.show()