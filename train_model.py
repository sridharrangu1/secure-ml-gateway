# train_model.py
import pandas as pd
import joblib
import os
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set absolute path to ensure consistency
mlflow.set_tracking_uri("mlruns")
mlflow.set_experiment("NoShow_Prediction_Experiment")

with mlflow.start_run() as run:
    print(f"Run started with ID: {run.info.run_id}")

    # 1. Load and preprocess
    df = pd.read_csv("KaggleV2-May-2016.csv")
    df["No-show"] = df["No-show"].map({"Yes": 1, "No": 0})

    features = ["Age", "Scholarship", "Hipertension", "Diabetes", "Alcoholism", "SMS_received"]
    X = df[features]
    y = df["No-show"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 2. Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 3. Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    # 4. Log metric
    mlflow.log_metric("accuracy", acc)

    # 5. Log model
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        registered_model_name="NoShow_RF"
    )

    # 6. Save for real-time API
    os.makedirs("app/models", exist_ok=True)
    joblib.dump(model, "app/models/noshow_model.pkl")

    print(f"Accuracy: {acc:.4f}")
    print("Model logged to MLflow and saved for Secure API Gateway.")
