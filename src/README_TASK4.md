# Task 4: Random Forest Hyperparameter Tuning and Champion Model Selection

## Objective

Tune Random Forest hyperparameters and select the best performing model (champion model) for crop yield prediction.

---

## Methodology

### 1. Hyperparameter Tuning

GridSearchCV was used to optimize the Random Forest model using TimeSeriesSplit cross-validation.

The following hyperparameters were tuned:

* `n_estimators`
* `max_depth`
* `min_samples_leaf`

The best hyperparameters obtained were:

* n_estimators = 100
* max_depth = 8
* min_samples_leaf = 1

---

### 2. Model Comparison

Three models were evaluated and compared:

1. Linear Regression
2. Default Random Forest
3. Tuned Random Forest

Evaluation metrics:

* Mean Absolute Error (MAE)
* R² Score

### Test Results

| Model                 | Test MAE | Test R² |
| --------------------- | -------: | ------: |
| Linear Regression     |    0.888 |   0.006 |
| Random Forest Default |    0.934 |  -0.164 |
| Random Forest Tuned   |    0.893 |  -0.071 |

---

### 3. Champion Model Selection

The Tuned Random Forest model was selected as the champion model after hyperparameter optimization.

The champion model was saved to:

```text
models/champion.joblib
```

---

## Files Created

### Source Files

```text
13_rf_tuning.py
14_model_comparison.py
15_select_champion.py
```

### Model Files

```text
models/random_forest_tuned.joblib
models/rf_best_params.json
models/champion.joblib
```

### Report Files

```text
reports/model_comparison.md
```

---

## Conclusion

Random Forest hyperparameters were successfully optimized using GridSearchCV. Model comparison was performed between Linear Regression, Default Random Forest, and Tuned Random Forest models. The tuned model was selected as the champion model and saved for future use.
