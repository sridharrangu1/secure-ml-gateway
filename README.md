# Secure ML API Gateway for CRM and Healthcare Systems

This project implements a **secure, AI-powered, cloud-aligned API system** to modernize CRM and healthcare service platforms. It integrates **machine learning models**, **DevOps automation**, and **role-based access control (RBAC)** to simulate a real-world AI deployment using FastAPI, MLflow, and GitHub Actions.

---

## Key Features

| Feature | Description |
|---------|-------------|
| **ML Predictions** | No-show prediction, billing anomaly detection, CRM churn prediction, patient clustering |
| **Secure API Gateway** | JWT-authenticated FastAPI microservices with role-based access (`admin`, `doctor`, `nurse`) |
| **DevOps Simulation** | CI/CD pipeline using GitHub Actions to retrain models on commit |
| **MLOps Tracking** | MLflow-based experiment tracking and model versioning |
| **Cloud-Native Ready** | Modular architecture, Dockerfile included, .env-secured |

---

## Machine Learning Modules

1. **Appointment No-Show Prediction** (RandomForest, XGBoost)
2. **Billing Anomaly Detection** (Isolation Forest, Autoencoder)
3. **CRM Churn Prediction** (XGBoost)
4. **Patient Clustering** (KMeans for personalization)

---

## API Endpoints (via FastAPI)

### `/predict_noshow` – POST

Predicts whether a patient will miss their appointment based on clinical and communication features.

#### Headers:
