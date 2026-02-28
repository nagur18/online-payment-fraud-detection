import pickle
import numpy as np
from functools import lru_cache
from flask import current_app


@lru_cache(maxsize=1)
def load_model():
    path = current_app.config["MODEL_PATH"]
    with open(path, "rb") as f:
        return pickle.load(f)


def predict_transaction(step, type_t, amount, oldbalanceOrg, newbalanceOrig):
    model = load_model()

    features = np.array([[step, type_t, amount, oldbalanceOrg, newbalanceOrig]])
    prob = model.predict_proba(features)[0][1]

    # business rules
    if amount > current_app.config["HIGH_AMOUNT_THRESHOLD"] and newbalanceOrig == 0:
        result = 1
    elif amount < current_app.config["SAFE_AMOUNT_THRESHOLD"] and (
        oldbalanceOrg - amount
    ) == newbalanceOrig:
        result = 0
    else:
        result = 1 if prob > current_app.config["FRAUD_THRESHOLD"] else 0

    return result, prob