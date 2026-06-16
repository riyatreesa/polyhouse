# Task 3: Random Forest Regression and Model Comparison

## Objective

Train a Random Forest Regressor to predict crop yield and compare its performance with the Linear Regression baseline using TimeSeriesSplit cross-validation.

---

## Methodology

1. Trained a Random Forest Regressor using:

   * Temperature
   * Humidity
   * CO₂ concentration

2. Evaluated the model using:

   * Mean Absolute Error (MAE)
   * R² Score

3. Compared Random Forest with Linear Regression using TimeSeriesSplit cross-validation.

4. Performed hyperparameter tuning using GridSearchCV.

5. Generated feature importance and prediction plots.

---

## Files Created

### Source Files

```text
src/09_train_random_forest.py
src/10_rf_cv_comparison.py
src/11_rf_hyperparameter_tuning.py
src/12_rf_champion_model.py
```

### Model Files

```text
models/random_forest.joblib
models/random_forest_tuned.joblib
models/rf_best_params.json
```

### Figures

```text
reports/figures/rf_importance.png
reports/figures/pred_vs_actual.png
```

---

## Cross-Validation Results

| Model               | Mean CV MAE |
| ------------------- | ----------- |
| Linear Regression   | 0.813 kg    |
| Random Forest       | 0.862 kg    |
| Tuned Random Forest | 0.841 kg    |

---

## Best Hyperparameters

* n_estimators = 100
* max_depth = 8
* min_samples_leaf = 1

---

## Outputs Generated

* Random Forest training script
* Feature importance chart
* TimeSeriesSplit cross-validation scores
* Hyperparameter tuning results
* Tuned Random Forest model
* Predicted vs Actual plot

---

## Conclusion

A Random Forest model was successfully trained and compared with the Linear Regression baseline. TimeSeriesSplit cross-validation was used to evaluate performance, and hyperparameter tuning improved the model. Feature importance analysis provided insights into the contribution of environmental variables to crop yield prediction.
