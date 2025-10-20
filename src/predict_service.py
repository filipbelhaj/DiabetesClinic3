from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from src.model_utils import ARTIFACTS_DIR
from pathlib import Path
import json

from src.model_utils import load_model

app = FastAPI(title="Virtual Diabetes Clinic: Progression Scoring API")

HIGH_RISK_THRESHOLD = 150.0


class PatientData(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

    model_config = {"extra": "forbid"}


@app.on_event("startup")
def _load_artifacts():
    try:
        artifacts = load_model()
        app.state.model = artifacts["model"]
        app.state.scaler = artifacts["scaler"]
        app.state.model_version = artifacts.get("version", "unknown")
    except Exception as e:
        # Fail fast if artifacts can't be loaded
        raise RuntimeError(f"Failed to load model artifact: {e}") from e


@app.get("/health")
def health():
    return {"status": "ok", "model_version": app.state.model_version}


@app.post("/predict")
def predict(payload: PatientData):
    try:
        X = np.asarray([[
            payload.age, payload.sex, payload.bmi, payload.bp,
            payload.s1, payload.s2, payload.s3, payload.s4, payload.s5, payload.s6
        ]], dtype=float)

        Xs = app.state.scaler.transform(X)
        yhat = float(app.state.model.predict(Xs)[0])

        response = {
            "prediction": yhat,
            "model_version": app.state.model_version,
        }

        if app.state.model_version == "v0.2":
            response["high_risk"] = yhat > HIGH_RISK_THRESHOLD

        return response

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

@app.get("/metrics")
def get_metrics():
    p: Path = ARTIFACTS_DIR / "metrics.json"
    if not p.exists():
        raise HTTPException(status_code=404, detail="metrics.json not found")
    return json.loads(p.read_text())
