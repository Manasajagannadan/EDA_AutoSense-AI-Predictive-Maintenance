<div align="center">

# 🚀 AutoSense AI: Intelligent Predictive Maintenance System

### End-to-End Machine Learning Pipeline | FastAPI | Streamlit | Render | GitHub Actions

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit)
![Render](https://img.shields.io/badge/Render-Deployed-success?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-blue?style=for-the-badge&logo=githubactions)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 🎯 Predict Machine Failures Before They Happen

**AutoSense AI** is a production-ready Machine Learning application that predicts industrial machine failures using sensor data.

The project demonstrates the complete AI lifecycle:

**Data → EDA → Feature Engineering → Machine Learning → FastAPI → Streamlit → Cloud Deployment**

Designed as a portfolio project showcasing production-oriented ML engineering skills.

</div>

---

# 🌐 Live Demo

## 🚀 Streamlit Dashboard

https://autosense-predictive-maintenance.streamlit.app/

Interactive web application for real-time machine failure prediction.

---

## ⚡ FastAPI Backend

https://autosense-ai-api.onrender.com

Production REST API serving machine learning predictions.

---

## 📖 Swagger API Documentation

https://autosense-ai-api.onrender.com/docs

Test API endpoints directly from your browser.

---

## 💻 GitHub Repository

https://github.com/Manasajagannadan/EDA_AutoSense-AI-Predictive-Maintenance

---

# 📌 Project Overview

Unexpected machine failures can cause:

- High maintenance costs
- Production downtime
- Equipment damage
- Reduced operational efficiency
- Financial losses

Traditional preventive maintenance performs servicing at fixed intervals regardless of the machine's condition.

AutoSense AI enables **Predictive Maintenance**, allowing maintenance teams to identify potential failures before they occur, reducing downtime and maintenance costs.

This project combines Machine Learning with a REST API and an interactive dashboard to deliver a production-ready predictive maintenance solution.

---

# ✨ Key Features

## 🤖 Machine Learning

- Industrial Machine Failure Prediction
- Failure Probability Estimation
- Risk Level Classification
- Maintenance Recommendation
- Feature Engineering
- Model Serialization using Joblib

---

## 🌐 Backend

- FastAPI REST API
- Automatic Swagger Documentation
- JSON API
- Input Validation using Pydantic
- Production-ready Prediction Service

---

## 📊 Dashboard

- Interactive Streamlit UI
- Real-Time Prediction
- User-Friendly Interface
- Cloud Hosted
- Easy Input Forms

---

## ☁ Deployment

- Render (FastAPI Backend)
- Streamlit Community Cloud
- GitHub Repository
- GitHub Actions CI

---

# 🏗 System Architecture

```text
                     User

                      │

                      ▼

          Streamlit Dashboard

                      │

          HTTP POST Request

                      │

                      ▼

             FastAPI REST API

                      │

            Load ML Model (.pkl)

                      │

              Feature Engineering

                      │

               Machine Learning

                      │

             Prediction Result

                      │

                      ▼

             JSON API Response

                      │

                      ▼

          Streamlit Visualization
```

---

# ⚙ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Data Visualization | Matplotlib, Seaborn |
| Backend Framework | FastAPI |
| API Server | Uvicorn |
| Dashboard | Streamlit |
| Model Serialization | Joblib |
| Deployment | Render |
| Frontend Hosting | Streamlit Community Cloud |
| Version Control | Git |
| Repository | GitHub |
| CI | GitHub Actions |

---

# 🚀 End-to-End Workflow

```text
Industrial Dataset

      │

      ▼

Exploratory Data Analysis

      │

      ▼

Feature Engineering

      │

      ▼

Model Training

      │

      ▼

Model Evaluation

      │

      ▼

Model Serialization

      │

      ▼

FastAPI Backend

      │

      ▼

Streamlit Dashboard

      │

      ▼

Cloud Deployment

      │

      ▼

End User Prediction
```

---

# 📊 Business Objective

The objective of this project is to predict machine failures before they occur, enabling organizations to:

- Reduce equipment downtime
- Optimize maintenance schedules
- Improve operational efficiency
- Lower maintenance costs
- Increase machine lifespan
- Support data-driven maintenance decisions

---

# ⭐ Project Highlights

- ✅ End-to-End Machine Learning Pipeline
- ✅ Industrial Predictive Maintenance Solution
- ✅ FastAPI REST API
- ✅ Interactive Streamlit Dashboard
- ✅ Cloud Deployment (Render + Streamlit)
- ✅ GitHub Actions Continuous Integration
- ✅ Production-Ready Architecture
- ✅ Resume & Interview Ready Project

---

# 📸 Application Preview

> **Home Page**
>
> *(Add Screenshot Here)*

---

> **Healthy Machine Prediction**
>
> *(Add Screenshot Here)*

---

> **Critical Failure Prediction**
>
> *(Add Screenshot Here)*

---

# 📑 What's Next?

The next section covers:

- 📂 Project Structure
- 📊 Dataset Description
- 🔍 Exploratory Data Analysis (EDA)
- 🛠 Feature Engineering
- 🤖 Machine Learning Pipeline
- 📈 Model Evaluation
- 🏆 Model Selection

# 📂 Project Structure

```text
EDA_AutoSense-AI-Predictive-Maintenance
│
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions CI Pipeline
│
├── app/
│   ├── main.py                   # FastAPI application
│   ├── schemas.py                # Request validation
│   └── utils.py                  # Model loading & prediction logic
│
├── dashboard/
│   └── streamlit_app.py          # Streamlit web application
│
├── dataset/
│   └── ai4i2020.csv              # Original dataset
│
├── models/
│   └── best_model.pkl            # Trained ML model
│
├── notebook/
│   └── Complete_EDA.ipynb        # Complete EDA & Model Development
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

## Dataset Name

**AI4I 2020 Predictive Maintenance Dataset**

The dataset contains industrial machine operational data collected from manufacturing environments.

The goal is to predict whether a machine is likely to fail based on its operating conditions.

---

## Features

| Feature | Description |
|----------|-------------|
| Type | Machine Type (L, M, H) |
| Air Temperature | Ambient Air Temperature (K) |
| Process Temperature | Process Temperature (K) |
| Rotational Speed | Rotational Speed (RPM) |
| Torque | Torque (Nm) |
| Tool Wear | Tool Wear (Minutes) |

---

## Target Variable

| Value | Meaning |
|--------|----------|
| 0 | Healthy Machine |
| 1 | Machine Failure |

---

# 🔍 Exploratory Data Analysis (EDA)

Before training the model, comprehensive Exploratory Data Analysis (EDA) was performed to understand the dataset.

The following analyses were conducted:

- Dataset Overview
- Data Types Inspection
- Missing Value Analysis
- Duplicate Record Check
- Statistical Summary
- Class Distribution
- Correlation Analysis
- Feature Distribution
- Outlier Detection
- Relationship Analysis

---

## Missing Value Analysis

The dataset was inspected for missing values.

```python
df.isnull().sum()
```

**Result**

✅ No missing values were found.

---

## Duplicate Records

Duplicate observations were checked using:

```python
df.duplicated().sum()
```

**Result**

✅ No duplicate records detected.

---

## Statistical Summary

Generated using:

```python
df.describe()
```

This helped understand:

- Mean
- Median
- Standard Deviation
- Minimum
- Maximum
- Quartiles

---

## Data Visualization

The following visualizations were created during EDA:

- Histograms
- Count Plots
- KDE Plots
- Box Plots
- Scatter Plots
- Pair Plots
- Correlation Heatmap

These visualizations helped identify patterns, distributions, and relationships between machine operating parameters.

---

# ⚙️ Feature Engineering

Feature Engineering was performed to improve the predictive capability of the machine learning model.

Additional domain-specific features were created.

---

## Engineered Features

| Feature | Description |
|----------|-------------|
| Thermal Stress Index | Process Temperature − Air Temperature |
| Temperature Ratio | Process Temperature ÷ Air Temperature |
| Operational Load Index | Torque × Rotational Speed |
| Wear Efficiency | Tool Wear ÷ Rotational Speed |
| Failure Risk Score | Torque × Tool Wear |

These engineered features capture hidden relationships between machine operating conditions.

---

# 🤖 Machine Learning Pipeline

The project follows a structured machine learning workflow.

```text
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Feature Engineering
   │
   ▼
Train-Test Split
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Best Model Selection
   │
   ▼
Model Serialization (.pkl)
   │
   ▼
FastAPI Deployment
   │
   ▼
Streamlit Dashboard
```

---

# 📈 Train-Test Split

The dataset was divided into:

- **Training Data:** 80%
- **Testing Data:** 20%

This ensures that the model is evaluated on unseen data.

---

# 🧠 Machine Learning Models Evaluated

Multiple machine learning algorithms were trained and compared.

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM
- CatBoost

Each model was evaluated using multiple performance metrics.

---

# 📏 Evaluation Metrics

The following metrics were used to compare model performance:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

These metrics provide a balanced assessment of classification performance, especially for predictive maintenance problems.

---

# 🏆 Best Model Selection

The final model was selected based on:

- Highest predictive performance
- Better generalization
- Faster inference time
- Robustness on unseen data

The trained model was serialized using **Joblib** and stored as:

```text
models/best_model.pkl
```

This model is loaded by the FastAPI backend for real-time predictions.

---

# 📌 Key Takeaways

- ✅ Clean and high-quality dataset
- ✅ Comprehensive Exploratory Data Analysis
- ✅ Domain-driven Feature Engineering
- ✅ Multiple ML Algorithms Compared
- ✅ Best Model Selected Based on Performance
- ✅ Production-ready Serialized Model

---

# 📑 Next Section

In the next section, we'll cover:

- 🚀 FastAPI Backend
- 🌐 REST API Architecture
- 📖 Swagger Documentation
- 🖥️ Streamlit Dashboard
- 🔄 API Integration
- 🧪 API Request & Response Examples

# 🚀 FastAPI Backend

The machine learning model is deployed as a REST API using **FastAPI**, providing high-performance real-time predictions.

## Why FastAPI?

- ⚡ High Performance
- 📖 Automatic Swagger Documentation
- ✅ Input Validation with Pydantic
- 🔄 RESTful API Design
- ☁ Easy Cloud Deployment
- 🏭 Production Ready

---

# 📂 Backend Structure

```text
app/

├── main.py
├── schemas.py
└── utils.py
```

| File | Purpose |
|------|----------|
| main.py | Creates FastAPI application and API endpoints |
| schemas.py | Defines request validation using Pydantic |
| utils.py | Loads trained model and performs prediction |

---

# 🤖 Model Loading

The trained model is loaded once when the API starts.

```python
MODEL_PATH = "models/best_model.pkl"

model = joblib.load(MODEL_PATH)
```

This avoids loading the model for every request and improves response time.

---

# 📡 API Endpoint

## POST `/predict`

Predicts whether a machine is likely to fail.

### Sample Request

```json
{
  "type": 0,
  "air_temperature": 298.2,
  "process_temperature": 308.7,
  "rotational_speed": 1408,
  "torque": 40,
  "tool_wear": 9
}
```

---

### Sample Response

```json
{
  "prediction": 1,
  "status": "Failure",
  "risk_level": "Critical",
  "failure_probability": 99.83,
  "recommendation": "Immediate maintenance required"
}
```

---

# 🌐 API Documentation

Interactive Swagger documentation is available at:

```
https://autosense-ai-api.onrender.com/docs
```

Using Swagger, you can:

- Test API endpoints
- View request schemas
- Inspect response formats
- Validate API functionality

---

# 🎨 Streamlit Dashboard

The frontend is built using **Streamlit**, allowing users to interact with the machine learning model through a simple web interface.

## Dashboard Features

- Enter machine operating parameters
- Predict machine failures
- Display failure probability
- Show risk level
- Provide maintenance recommendations

---

# 🌍 Live Application

### 🚀 Streamlit Dashboard

https://autosense-predictive-maintenance.streamlit.app/

### ⚡ FastAPI API

https://autosense-ai-api.onrender.com

### 📖 Swagger API

https://autosense-ai-api.onrender.com/docs

---

# ⚙ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Manasajagannadan/EDA_AutoSense-AI-Predictive-Maintenance.git
```

Move into the project directory:

```bash
cd EDA_AutoSense-AI-Predictive-Maintenance
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run FastAPI

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 5️⃣ Run Streamlit

Open another terminal and execute:

```bash
streamlit run dashboard/streamlit_app.py
```

The dashboard will open at:

```
http://localhost:8501
```

---

# 🖥 How to Use

### Step 1

Open the Streamlit dashboard.

---

### Step 2

Enter the following machine parameters:

- Machine Type
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

---

### Step 3

Click:

```
Predict Failure
```

---

### Step 4

The application sends the input to the FastAPI backend.

---

### Step 5

The machine learning model predicts the result.

---

### Step 6

View:

- Machine Status
- Failure Probability
- Risk Level
- Maintenance Recommendation

---

# 🔄 Application Workflow

```text
User Input

      │

      ▼

Streamlit Dashboard

      │

      ▼

FastAPI REST API

      │

      ▼

Load Trained Model

      │

      ▼

Prediction

      │

      ▼

JSON Response

      │

      ▼

Dashboard Result
```

---

# 📌 Highlights

- REST API using FastAPI
- Interactive Streamlit Dashboard
- Cloud-hosted Backend
- Real-time Prediction
- Production-ready Inference
- Clean Project Structure
- Recruiter-Friendly Portfolio Project

---

# 📑 Next Section

The next part includes:

- ☁ Deployment Architecture
- 🚀 Render Deployment
- 🌐 Streamlit Community Cloud Deployment
- ⚙ GitHub Actions CI/CD
- 📸 Screenshots
- 🔧 Troubleshooting Guide
- 📈 Future Improvements

# ☁️ Cloud Deployment

This project is fully deployed to the cloud, allowing users to access the application without installing any software locally.

---

# 🌍 Deployment Architecture

```text
                    GitHub Repository
                           │
         ┌─────────────────┴─────────────────┐
         │                                   │
         ▼                                   ▼
  Render Web Service              Streamlit Community Cloud
   (FastAPI Backend)                (Frontend Dashboard)
         │                                   │
         └─────────────── API Calls ─────────┘
                         │
                         ▼
                Machine Learning Model
                         │
                         ▼
                  Prediction Response
```

---

# 🚀 Live Deployment

## 🌐 Streamlit Dashboard

Interactive Web Application

https://autosense-predictive-maintenance.streamlit.app/

---

## ⚡ FastAPI Backend

REST API

https://autosense-ai-api.onrender.com

---

## 📖 Swagger Documentation

Interactive API Documentation

https://autosense-ai-api.onrender.com/docs

---

## 💻 GitHub Repository

https://github.com/Manasajagannadan/EDA_AutoSense-AI-Predictive-Maintenance

---

# 🔄 Deployment Workflow

```text
Developer

      │

      ▼

Push Code to GitHub

      │

      ▼

GitHub Repository

      │

      ├──────────────► GitHub Actions

      │                     │

      │                     ▼

      │               CI Validation

      │

      ▼

Render Deployment

      │

      ▼

FastAPI API

      │

      ▼

Streamlit Dashboard

      │

      ▼

End Users
```

---

# ⚙ GitHub Actions (CI)

This project includes a GitHub Actions workflow to automate Continuous Integration (CI).

Current workflow performs:

- Repository validation
- Dependency installation
- Python environment setup
- Build verification

Workflow file:

```text
.github/workflows/ci.yml
```

Benefits:

- Detects dependency issues early
- Validates every push
- Ensures project builds successfully
- Supports collaborative development

---

# 📸 Application Screenshots

## 🏠 Home Page

> *(Add Screenshot Here)*

---

## ✅ Healthy Machine Prediction

> *(Add Screenshot Here)*

---

## 🚨 Critical Failure Prediction

> *(Add Screenshot Here)*

---

## 📖 Swagger API Documentation

> *(Add Screenshot Here)*

---

# 🔧 Troubleshooting

## Problem

### FastAPI is not starting

Solution

```bash
uvicorn app.main:app --reload
```

---

## Problem

### Streamlit cannot connect to API

Check whether the FastAPI server is running.

Local API URL

```text
http://127.0.0.1:8000
```

Cloud API URL

```text
https://autosense-ai-api.onrender.com
```

---

## Problem

### Render API timeout

Render Free Tier services automatically sleep after inactivity.

If the first prediction takes longer than expected:

1. Open

https://autosense-ai-api.onrender.com/docs

2. Wait until the API loads.

3. Return to Streamlit and retry.

---

## Problem

### Model not found

Ensure the trained model exists.

```text
models/
    best_model.pkl
```

---

## Problem

### Missing dependencies

Install required packages.

```bash
pip install -r requirements.txt
```

---

# 📈 Performance Summary

| Metric | Status |
|----------|--------|
| Machine Learning Model | ✅ Completed |
| FastAPI Backend | ✅ Completed |
| Streamlit Dashboard | ✅ Completed |
| Cloud Deployment | ✅ Completed |
| GitHub Actions | ✅ Completed |
| REST API | ✅ Completed |
| Swagger Documentation | ✅ Completed |
| End-to-End Integration | ✅ Completed |

---

# 🧪 Testing

The project has been tested for:

- Local FastAPI execution
- Local Streamlit execution
- API integration
- Cloud deployment
- Live predictions
- Swagger API
- GitHub repository
- GitHub Actions workflow

---

# 💼 Portfolio Highlights

This project demonstrates practical experience in:

- Machine Learning
- Feature Engineering
- REST API Development
- FastAPI
- Streamlit
- Cloud Deployment
- GitHub Actions
- Git Version Control
- End-to-End ML Pipelines

---

# 🎯 Learning Outcomes

Through this project, the following skills were developed:

- Data preprocessing
- Exploratory Data Analysis
- Feature engineering
- Model training and evaluation
- API development
- Dashboard development
- Cloud deployment
- Continuous Integration
- Production-ready ML workflows

---

# 🚀 Production Improvements (Future Scope)

Potential enhancements include:

- Docker containerization
- Kubernetes deployment
- CI/CD with automated deployment
- MLflow for experiment tracking
- Model versioning
- User authentication
- Database integration
- Prediction history
- Monitoring and logging
- Explainable AI (SHAP dashboard)
- Model retraining pipeline
- Cloud deployment on AWS/Azure/GCP

---

# 📑 Next Section

The final section includes:

- Resume-ready project summary
- Recruiter highlights
- Interview discussion points
- Contributing guidelines
- License
- Author information
- Contact details
- Acknowledgements

# 🚀 Future Enhancements

The current project demonstrates a complete end-to-end Machine Learning deployment pipeline. Future enhancements can further improve scalability, usability, and production readiness.

## Planned Improvements

- 🐳 Docker Containerization
- ☁ Deploy on AWS / Azure / Google Cloud
- 🔄 Automated CI/CD Pipeline
- 📊 MLflow Experiment Tracking
- 📝 Prediction History Database
- 👥 User Authentication & Authorization
- 📈 Model Monitoring Dashboard
- 📢 Email/SMS Failure Alerts
- 📂 Model Versioning
- 🔍 Explainable AI (SHAP Dashboard)
- 📱 Mobile Responsive Dashboard
- 🔄 Automatic Model Retraining Pipeline

---

# 🛣 Roadmap

- [x] Data Cleaning
- [x] Exploratory Data Analysis
- [x] Feature Engineering
- [x] Machine Learning Model
- [x] FastAPI Backend
- [x] Streamlit Dashboard
- [x] Render Deployment
- [x] Streamlit Community Cloud Deployment
- [x] GitHub Actions CI
- [ ] Docker Support
- [ ] MLflow Integration
- [ ] Kubernetes Deployment
- [ ] AWS Deployment
- [ ] Monitoring & Logging

---

# 💼 Resume Project Summary

### AutoSense AI – Intelligent Predictive Maintenance System

Designed and developed a production-ready Machine Learning application for industrial predictive maintenance. The project predicts machine failures using sensor data and provides real-time failure probability, risk assessment, and maintenance recommendations through an interactive Streamlit dashboard powered by a FastAPI backend.

### Key Contributions

- Developed an end-to-end Machine Learning pipeline.
- Performed Exploratory Data Analysis (EDA) and Feature Engineering.
- Trained and evaluated multiple classification models.
- Built REST APIs using FastAPI.
- Developed an interactive Streamlit dashboard.
- Deployed backend on Render.
- Deployed frontend on Streamlit Community Cloud.
- Implemented GitHub Actions for Continuous Integration.
- Built a production-ready cloud-based AI application.

---

# 🎯 Skills Demonstrated

## Machine Learning

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Classification
- Model Evaluation
- Model Serialization

---

## Backend Development

- FastAPI
- REST APIs
- Pydantic Validation
- JSON APIs

---

## Frontend

- Streamlit
- Interactive Dashboards
- Data Visualization

---

## Cloud & DevOps

- Render
- Streamlit Community Cloud
- Git
- GitHub
- GitHub Actions (CI)

---

## Programming

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

# 🎯 Interview Discussion Points

This project demonstrates knowledge in:

- End-to-End Machine Learning Pipeline
- Production ML Deployment
- REST API Development
- FastAPI
- Streamlit
- Feature Engineering
- Model Deployment
- Cloud Hosting
- GitHub Actions CI
- Software Engineering Best Practices

Typical interview topics this project supports:

- Explain the Machine Learning lifecycle.
- Why was FastAPI chosen over Flask?
- How does the Streamlit dashboard communicate with the backend?
- Explain the feature engineering process.
- How is the model loaded efficiently?
- How would you scale this project for enterprise use?
- What improvements would you make for production deployment?

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature/your-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature/your-feature
```

5. Open a Pull Request.

---

# 🐛 Issues

If you find any bugs or have feature requests, please open an issue in the GitHub repository.

GitHub Repository:

https://github.com/Manasajagannadan/EDA_AutoSense-AI-Predictive-Maintenance

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project with proper attribution.

---

# 👩‍💻 Author

## Manasa

**AI Engineer | Machine Learning Engineer | Python Developer**

### Connect with me

**GitHub**

https://github.com/Manasajagannadan

**LinkedIn**

> *(Add your LinkedIn profile URL here.)*

---

# 🙏 Acknowledgements

Special thanks to:

- AI4I 2020 Predictive Maintenance Dataset
- Scikit-learn
- FastAPI
- Streamlit
- Render
- GitHub
- Open Source Community

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository on GitHub.

🍴 Fork it to build your own version.

📢 Share it with others interested in Machine Learning and Predictive Maintenance.

---

<div align="center">

## 🚀 AutoSense AI

**Predict • Prevent • Perform**

Made with ❤️ using Python, Machine Learning, FastAPI, Streamlit, and Cloud Technologies.

</div>
