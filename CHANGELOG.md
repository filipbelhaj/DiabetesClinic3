# Changelog

## v0.2
- **Model:** `StandardScaler + Ridge(alpha=1.0)`
- **Why:** L2 regularization makes it more stable than OLS.
- **API:** Unchanged; response includes `model_version="v0.2"` and, if threshold is crossed, `high_risk`.
- **Results:** See `artifacts/metrics.json`.

## v0.1
- **Model:** `StandardScaler + LinearRegression`
- **API:** `/health`, `/predict`
- **Artifacts:** `model/model_v0.1.pkl`, `artifacts/metrics.json`


