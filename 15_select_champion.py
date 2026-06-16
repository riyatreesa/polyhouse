from joblib import load, dump

# Load tuned RF
champion = load(
    "models/random_forest_tuned.joblib"
)

# Save champion model
dump(
    champion,
    "models/champion.joblib"
)

print("Champion model saved.")
print("Saved: models/champion.joblib")

print(
    "Justification:"
)
print(
    "Tuned Random Forest selected as champion model because "
    "it achieved the best overall performance after hyperparameter tuning."
)