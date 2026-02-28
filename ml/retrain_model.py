import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

def retrain_model(data_path="data.csv"):
    df = pd.read_csv(data_path)

    X = df[["step", "type", "amount", "oldbalanceOrg", "newbalanceOrig"]]
    y = df["isFraud"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model retrained successfully")

if __name__ == "__main__":
    retrain_model()