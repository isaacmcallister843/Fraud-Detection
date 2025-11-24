# app.py
import os, json, joblib, pickle, pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any, List
import numpy as np
from contextlib import asynccontextmanager
from typing import Literal, Annotated
from pathlib import Path

# All imports for our model and pipeline to work correctly - pickle models needs access to all its parts 
import sklearn 
from sklearn import set_config
from transforms import drop_func, to_float32
set_config(transform_output="pandas")

# Resolve path 
ROOT = Path(__name__).resolve().parent
os.chdir(ROOT)

# Set all globals to none
schema = None
model = None 
thresh = None

# Define our input scheme (would be cool if we could do this dynamically)
class PredictRequest(BaseModel):
    income: float
    name_email_similarity: float
    customer_age: float
    days_since_request: float
    intended_balcon_amount: float

    payment_type: Literal['AA', 'AB', 'AC', 'AD', 'AE']
    velocity_6h: float
    velocity_24h: float
    velocity_4w: float
    bank_branch_count_8w: float
    date_of_birth_distinct_emails_4w: float

    employment_status: Literal['CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG']
    credit_risk_score: float
    email_is_free: Annotated[int, Field(strict=True, ge=0, le=1)]
    housing_status: Literal['BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG']
    phone_home_valid: Annotated[int, Field(strict=True, ge=0, le=1)]
    phone_mobile_valid: Annotated[int, Field(strict=True, ge=0)]
    has_other_cards: Annotated[int, Field(strict=True, ge=0, le=1)]
    proposed_credit_limit: float
    foreign_request: Annotated[int, Field(strict=True, ge=0, le=1)]
    source: Annotated[int, Field(strict=True, ge=0, le=1)]
    session_length_in_minutes: float
    device_os: Literal['linux', 'macintosh', 'other', 'windows', 'x11']
    keep_alive_session: Annotated[int, Field(strict=True, ge=0, le=1)]
    device_distinct_emails_8w: float
    month_sin: float
    month_cos: float

class PredictResponse(BaseModel): 
    predict : int 
    predict_proba : float 
    threshold: float 

@asynccontextmanager
async def lifespan(app: FastAPI):
    _load_artifacts()
    yield

def _predict_df(df: pd.DataFrame):
    proba = model.predict_proba(df)[:, 1]
    pred = int(proba >= thresh)
    return float(proba), pred, thresh


def _load_artifacts():
    global schema
    global model 
    global thresh 

    with open('artifacts/feature_schema.json', 'r') as file:
        schema = json.loads(file.read())
    
    with open('artifacts/threshold.json', 'r') as file:
        thresh = float(json.loads(file.read())['threshold'])
    
    model = joblib.load("artifacts/fraud_model.pkl")


app = FastAPI(title="Fraud Model API", version="v1", lifespan=lifespan)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/request_schema")
def get_schema():
    return schema 

@app.post('/predict')
def predict(req: PredictRequest):
    X = pd.DataFrame(req, index=[0])
    proba, pred, thresh  = _predict_df(X)
    return PredictResponse(predict = pred, predict_proba=proba, threshold = thresh) 