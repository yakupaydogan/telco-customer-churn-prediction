from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import joblib
import pandas as pd
from pydantic import BaseModel
import numpy as np

app = FastAPI()

templates = Jinja2Templates(directory="templates")

model = joblib.load('telco_churn_xgb_final.pkl')
bootstrap_models = joblib.load("bootstrap_models.pkl")
CI_LEVEL = 95

def calc_ci(models, X_one, ci=95):
    probs = np.array([m.predict_proba(X_one)[:, 1][0] for m in models])
    mean = float(probs.mean())
    alpha = (100 - ci) / 2
    lower = float(np.percentile(probs, alpha))
    upper = float(np.percentile(probs, 100 - alpha))
    return mean, lower, upper

class CustomerFeatures(BaseModel):
    gender: str
    SeniorCitizen: str
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(features : CustomerFeatures):
    input_data = pd.DataFrame([features.model_dump()])

    cols = [
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies'
    ]

    for col in cols:
        input_data[col] = input_data[col].replace('No internet service','No')

    input_data['MultipleLines'] = input_data['MultipleLines'].replace('No phone service', 'No')

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0, 1]

    mean_prob, ci_lower, ci_upper = calc_ci(
        bootstrap_models,
        input_data,
        ci=CI_LEVEL
    )

    return {
        "churn_probability": round(mean_prob, 4),
       #"churn_probability": round(float(probability), 4),
        "ci_level": CI_LEVEL,
        "ci_lower": round(ci_lower, 4),
        "ci_upper": round(ci_upper, 4)
    }