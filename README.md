# Secure ML API Gateway for CRM and Healthcare Systems

This project demonstrates a production-ready, secure, and modular API-driven ML architecture for appointment no-show prediction using real tools such as FastAPI, MLflow, and GitHub Actions. It is part of a broader system titled:

**“AI-Powered Cloud Transformation for CRM and Healthcare Systems: Secure Data Integration, DevOps Automation, and Cloud-Native Business Modernization.”**

---

## Key Features

### 1. Secure API Gateway
- Built using **FastAPI**
- JWT-based **token authentication** with role-based access control
- Access logging for each request
- Simulated microservice: `/predict_noshow`

### 2. ML Model Integration
- Random Forest model trained on real patient appointment data
- Features: `Age`, `Scholarship`, `Hypertension`, `Diabetes`, `Alcoholism`, `SMS_received`
- Model saved using `joblib` and loaded inside FastAPI route
- Prediction output: `0 = will show`, `1 = no-show likely`

### 3. DevOps Automation & CI/CD
- **MLflow** tracking with:
  - Accuracy logging
  - Model versioning
  - Registered artifacts
- **GitHub Actions** workflow (`.github/workflows/ml-train.yml`) to auto-train model on every push
- Dockerfile included for containerization
- .env-based secret management

---


## ⚙Setup Instructions

```bash
# Step 1: Install Python dependencies
pip install -r requirements.txt

# Step 2: Train model and log to MLflow
python train_model.py

# Step 3: Launch MLflow UI
mlflow ui --port 5000

# Step 4: Generate a token
python token_gen.py

# Step 5: Run the FastAPI app
uvicorn app.main:app --reload

