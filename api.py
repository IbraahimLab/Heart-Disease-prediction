from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = joblib.load('random_forest_model.pkl')

# Define the input data model
class HeartData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

@app.post("/predict")
def predict(data: HeartData):
    features = np.array([[data.age, data.sex, data.cp, data.trestbps, data.chol, data.fbs,
                         data.restecg, data.thalach, data.exang, data.oldpeak, data.slope, data.ca, data.thal]])
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}
