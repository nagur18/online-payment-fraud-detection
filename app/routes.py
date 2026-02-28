from flask import Blueprint, render_template, request
import logging

from .services.predictor import predict_transaction

main = Blueprint("main", __name__)
logger = logging.getLogger(__name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/predict")
def predict():
    return render_template("predict.html")


@main.route("/submit", methods=["POST"])
def submit():
    try:
        step = float(request.form.get("step", 0))
        type_t = float(request.form.get("type", 0))
        amount = float(request.form.get("amount", 0))
        oldbalanceOrg = float(request.form.get("oldbalanceOrg", 0))
        newbalanceOrig = float(request.form.get("newbalanceOrig", 0))

        # ✅ ONLY call service layer
        result, prob = predict_transaction(
            step, type_t, amount, oldbalanceOrg, newbalanceOrig
        )

        return render_template("submit.html", result=result, prob=prob)

    except Exception as e:
        logger.exception("Prediction failed")
        return render_template("error.html", message=str(e)), 500