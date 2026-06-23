from fastapi import FastAPI
from app.schemas import MachineInput
from app.utils import load_model

import pandas as pd

app = FastAPI(
    title="Predictive Maintenance API",
    version="1.0"
)

model = load_model()


@app.get("/")
def home():

    return {
        "message": "Predictive Maintenance API Running"
    }

@app.get("/model-info")
def model_info():

    return {

        "model": "LightGBM",

        "accuracy": "99.25%",

        "precision": "93.44%",

        "recall": "83.82%",

        "f1_score": "88.37%"
    }
@app.post("/predict")
def predict(data: MachineInput):

    df = pd.DataFrame([data.dict()])

    prediction = int(model.predict(df)[0])

    probability = float(
        model.predict_proba(df)[0][1]
    )

    # Risk Level
    if probability < 0.20:
        risk_level = "Low"
        recommendation = "Machine operating normally"

    elif probability < 0.70:
        risk_level = "Medium"
        recommendation = "Schedule preventive maintenance"

    else:
        risk_level = "Critical"
        recommendation = "Immediate maintenance required"

    status = (
        "Failure"
        if prediction == 1
        else "Healthy"
    )

    return {
        "prediction": prediction,
        "status": status,
        "risk_level": risk_level,
        "failure_probability": round(probability * 100, 2),
        "recommendation": recommendation
    }

@app.get("/health")
def health():

    return {

        "status": "healthy",

        "model_loaded": True
    }