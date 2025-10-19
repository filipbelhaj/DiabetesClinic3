from __future__ import annotations

import json
from pathlib import Path
import joblib

MODELS_DIR = Path("model")
ARTIFACTS_DIR = Path("artifacts")


def save_model(artifacts, version: str) -> None:
    MODELS_DIR.mkdir(exist_ok=True)
    joblib.dump(artifacts, MODELS_DIR / f"model_{version}.pkl")


def load_model(version: str | None = None):
    if version:
        path = MODELS_DIR / f"model_{version}.pkl"
    else:
        models = sorted(MODELS_DIR.glob("model_*.pkl"))
        if not models:
            raise FileNotFoundError("No model artifacts found.")
        path = models[-1]
    return joblib.load(path)


def save_metrics(metrics: dict) -> None:
    ARTIFACTS_DIR.mkdir(exist_ok=True)
    (ARTIFACTS_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2))


