from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load model once (IMPORTANT)
model = joblib.load("model.pkl")


class InputData(BaseModel):
    hours_studied: float
    attendance: float


@app.post("/predict")
def predict(data: InputData):
    features = [[data.hours_studied, data.attendance]]
    prediction = model.predict(features)

    return {"prediction": "Pass" if int(prediction[0]) else "Fail"}
