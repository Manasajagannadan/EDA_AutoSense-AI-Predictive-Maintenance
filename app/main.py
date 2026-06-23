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

# @app.post("/predict")
# def predict(data: MachineInput):

#     df = pd.DataFrame([data.dict()])

#     prediction = model.predict(df)[0]

#     probability = float(
#         model.predict_proba(df)[0][1]
#     )

#     return {

#         "prediction": int(prediction),

#         "failure_probability": round(
#             probability,
#             4
#         )
#     }


# from fastapi import FastAPI
# from pydantic import BaseModel
# import pandas as pd
# import joblib

# app = FastAPI()

# model = joblib.load("model/best_model.pkl")

# class MachineData(BaseModel):

#     Type:int
#     Air_temperature_K:float
#     Process_temperature_K:float
#     Rotational_speed_rpm:float
#     Torque_Nm:float
#     Tool_wear_min:float

#     Thermal_Stress_Index:float
#     Wear_Efficiency:float
#     Operational_Load_Index:float
#     Temperature_Ratio:float
#     Failure_Risk_Score:float

# @app.get("/")
# def home():

#     return {
#         "message":"Predictive Maintenance API"
#     }

# @app.post("/predict")
# def predict(data: MachineData):

#     df = pd.DataFrame([data.dict()])

#     prediction = model.predict(df)[0]

#     probability = float(
#         model.predict_proba(df)[0][1]
#     )

#     return {
#         "prediction": int(prediction),
#         "failure_probability": probability
#     }