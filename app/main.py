# app/main.py
from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel
from app.auth import decode_token
from app.logger import log_access
from app.roles import PERMISSIONS
import joblib
import os

app = FastAPI(title="Secure ML API Gateway")

# Load model
model_path = os.path.join("app", "models", "noshow_model.pkl")
model = joblib.load(model_path)

# Pydantic model for input
class NoShowFeatures(BaseModel):
    Age: int
    Scholarship: int
    Hipertension: int
    Diabetes: int
    Alcoholism: int
    SMS_received: int

# Auth logic
def authorize_user(x_token: str = Header(...)):
    payload = decode_token(x_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token invalid or expired")
    return payload

@app.get("/")
def root():
    return {"message": "Secure ML API Gateway is live."}

@app.post("/predict_noshow")
def predict_no_show(data: NoShowFeatures, user=Depends(authorize_user)):
    role = user["role"]
    user_id = user["sub"]

    if "predict_noshow" not in PERMISSIONS.get(role, []):
        log_access(user_id, role, "predict_noshow", "denied")
        raise HTTPException(status_code=403, detail="Access denied")

    features = [[
        data.Age, data.Scholarship, data.Hipertension,
        data.Diabetes, data.Alcoholism, data.SMS_received
    ]]
    prediction = int(model.predict(features)[0])

    log_access(user_id, role, "predict_noshow", "allowed")

    return {
        "user": user_id,
        "role": role,
        "prediction": prediction,
        "description": "1 = No-show likely, 0 = Will show"
    }
