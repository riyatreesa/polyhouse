import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Columns for correlation
features = ["temperature_c", "humidity_pct", "co2_ppm", "yield_kg"]

# Calculate correlation matrix
corr_matrix = df[features].corr()

# Print values to verify
print(corr_matrix)

# Create heatmap
fig, ax = plt.subplots(figsize=(6, 5))

im = ax.imshow(
    corr_matrix,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

# Axis labels
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

# Color bar
fig.colorbar(im, ax=ax, label="Pearson r")

# Title
ax.set_title("Sensor & Yield Correlations")

plt.tight_layout()

# Save image
plt.savefig(
    "reports/figures/corr_heatmap.png",
    dpi=150
)

plt.show()