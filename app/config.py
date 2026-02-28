import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")
    MODEL_PATH = os.environ.get("MODEL_PATH", "model.pkl")
    FRAUD_THRESHOLD = 0.05
    HIGH_AMOUNT_THRESHOLD = 100000
    SAFE_AMOUNT_THRESHOLD = 5000