import pandas as pd
from joblib import load

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Load data
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Features and target
X = df[["temperature_c", "humidity_pct", "co2_ppm"]]
y = df["yield_kg"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------
# Linear Regression
# -------------------------
linear = LinearRegression()
linear.fit(X_train, y_train)

linear_pred = linear.predict(X_test)

linear_mae = mean_absolute_error(y_test, linear_pred)
linear_r2 = r2_score(y_test, linear_pred)

# -------------------------
# Default RF
# -------------------------
rf_default = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_default.fit(X_train, y_train)

rf_pred = rf_default.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_r2 = r2_score(y_test, rf_pred)

# -------------------------
# Tuned RF
# -------------------------
rf_tuned = load(
    "models/random_forest_tuned.joblib"
)

tuned_pred = rf_tuned.predict(X_test)

tuned_mae = mean_absolute_error(y_test, tuned_pred)
tuned_r2 = r2_score(y_test, tuned_pred)

# Comparison table
results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest Default",
        "Random Forest Tuned"
    ],
    "Test MAE": [
        linear_mae,
        rf_mae,
        tuned_mae
    ],
    "Test R²": [
        linear_r2,
        rf_r2,
        tuned_r2
    ]
})

print(results)

# Save markdown report
with open("reports/model_comparison.md", "w") as f:
    f.write(results.to_markdown(index=False))

print("Saved: reports/model_comparison.md")