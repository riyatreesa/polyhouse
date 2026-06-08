from pathlib import Path
import pandas as pd

# Load cleaned dataset
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Summary statistics
summary = df[["temperature", "humidity", "co2", "yield"]].describe().T
summary["cv"] = summary["std"] / summary["mean"]

# Rule violations
temp_violations = (df["temperature"] < 0).sum()
humidity_violations = (df["humidity"] > 100).sum()
co2_violations = (df["co2"] < 0).sum()
yield_violations = (df["yield"] < 0).sum()

# Build report
report = []

report.append("# Polyhouse Data Quality Report\n")
report.append(f"Rows: {len(df)}\n")

report.append("\nSUMMARY STATISTICS\n")
report.append(summary.to_string())

report.append("\n\nRULE VIOLATIONS\n")
report.append(f"Temperature < 0°C: {temp_violations}")
report.append(f"Humidity > 100%: {humidity_violations}")
report.append(f"CO2 < 0: {co2_violations}")
report.append(f"Yield < 0: {yield_violations}")

# Create reports folder if it does not exist
Path("reports").mkdir(exist_ok=True)

# Save report
Path("reports/data_quality.md").write_text(
    "\n".join(report),
    encoding="utf-8"
)

print("Data quality report saved to reports/data_quality.md")