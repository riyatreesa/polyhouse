import pandas as pd
import json
import joblib

from sklearn.model_selection import (
    train_test_split,
    TimeSeriesSplit,
    GridSearchCV
)

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

# TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=3)

# Grid
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 8, 16],
    "min_samples_leaf": [1, 3, 5],
}

rf = RandomForestRegressor(
    random_state=42,
    n_jobs=-1
)

search = GridSearchCV(
    rf,
    param_grid,
    cv=tscv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1,
    refit=True
)

search.fit(X_train, y_train)

print("Best params:", search.best_params_)
print("Best CV MAE:", round(-search.best_score_, 3))

# Save tuned model
joblib.dump(
    search.best_estimator_,
    "models/random_forest_tuned.joblib"
)

# Save parameters
with open("models/rf_best_params.json", "w") as f:
    json.dump(search.best_params_, f, indent=2)