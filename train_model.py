# train_model.py
import pandas as pd
import joblib
import os
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Enable MLflow autologging
mlflow.set_tracking_uri("file:///tmp/mlruns")  # local storage
mlflow.set_experiment("NoShow_Prediction_Experiment")

with mlflow.start_run():

    # Load and preprocess
    df = pd.read_csv("KaggleV2-May-2016.csv")
    df["No-show"] = df["No-show"].map({"Yes": 1, "No": 0})
    features = ["Age", "Scholarship", "Hipertension", "Diabetes", "Alcoholism", "SMS_received"]
    X = df[features]
    y = df["No-show"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    # Log metrics & model
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, artifact_path="rf_model")

    # Save for API gateway
    os.makedirs("app/models", exist_ok=True)
    joblib.dump(model, "app/models/noshow_model.pkl")

    print("Model trained, logged to MLflow, and saved to app/models/")
