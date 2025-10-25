# 🧠 AI-Driven Predictive Analytics Platform (MLOps)

An end-to-end **MLOps project** that integrates data generation, model training, containerization, and automated deployment using **GitHub Actions** and **Docker**.  
This project demonstrates how to build, train, and deploy an AI model with a fully automated CI/CD workflow.

---

## 🚀 Project Overview

This project showcases the full lifecycle of an AI model:
1. Generating synthetic datasets  
2. Training a predictive model  
3. Serving the model through a Flask web application  
4. Containerizing the app using Docker  
5. Automating the build and deployment using GitHub Actions

---

## 🧩 Project Structure

MLOpsProject/
│
├── data.py # Generates synthetic dataset
├── train_model.py # Trains the ML model
├── app/
│ └── app.py # Flask app serving predictions
├── Dockerfile # Docker configuration
├── requirements.txt # Python dependencies
├── main.py # Entry point for local testing
└── .github/workflows/
└── mlops-ci.yml # GitHub Actions workflow for CI/CD



---

## ⚙️ How It Works

### 1️⃣ Data Generation  
`data.py` creates a synthetic dataset using pandas and stores it locally for model training.

### 2️⃣ Model Training  
`train_model.py` trains a regression model (using scikit-learn) and saves the trained model as `model.pkl`.

### 3️⃣ Web Application  
A lightweight Flask app (`app.py`) loads the trained model and exposes an endpoint for predictions.

### 4️⃣ Dockerization  
The `Dockerfile` builds a portable image of the entire app, making deployment consistent across environments.

### 5️⃣ CI/CD Automation  
GitHub Actions automates:
- Dependency installation  
- Data generation  
- Model training  
- Docker image build  
- Deployment to a self-hosted VM runner

---

## 🐳 Docker Commands

```bash
# Build Docker image
docker build -t mlops-app .

# Run the container
docker run -d -p 5000:5000 mlops-app



After running, open your browser at:
👉 http://localhost:5000

🔁 CI/CD Pipeline (GitHub Actions)

Automatically runs whenever code is pushed to the main branch.
Rebuilds and redeploys the application inside the VM using the self-hosted runner.

Workflow file: .github/workflows/mlops-ci.yml

🧠 Tech Stack
Component	Technology Used
Language	Python 3.9
ML Library	scikit-learn
Web Framework	Flask
Containerization	Docker
Automation	GitHub Actions
Environment	Self-hosted Runner (VM)
📊 Key Learning Outcomes

✅ End-to-end MLOps pipeline implementation
✅ CI/CD automation with GitHub Actions
✅ Containerization and deployment using Docker
✅ Model serving via REST API
✅ Practical hands-on AI workflow automation

📘 Author

Abu Jor Al Gefari (Ibne Sabid Saikat)
🚀 Microsoft Student Ambassador | AZ-104 Certified | Cloud & DevOps Enthusiast
🔗 Medium Article

⭐ If you found this helpful, give this repo a star!
