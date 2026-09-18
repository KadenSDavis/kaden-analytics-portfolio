Employee Attrition Prediction (XGBoost + SHAP Explainability)

This project predicts employee attrition using the IBM HR Analytics dataset. It demonstrates a complete data science workflow — from data preprocessing and feature engineering to model training, evaluation, and explainability.

🎯 Project Objectives

Identify the key drivers of employee attrition.

Build a predictive model using XGBoost.

Explain model decisions using SHAP.

Visualize attrition patterns by department and tenure.

Provide actionable insights for HR teams.

📂 Repository Structure

employee-attrition-ml/
│
├── data/
│   └── HR-Employee-Attrition.csv
│
├── notebooks/
│   └── attrition_analysis.py
│
├── visuals/
│   ├── shap_summary.png
│   ├── attrition_by_department.png
│   └── attrition_by_tenure.png
│
└── README.md

📊 Dataset Overview

The dataset includes 1,470 employees and 35+ HR features, covering:

Demographics (Age, Gender, MaritalStatus)

Job characteristics (JobRole, Department, JobLevel)

Compensation (MonthlyIncome, StockOptionLevel)

Satisfaction metrics (JobSatisfaction, EnvironmentSatisfaction)

Tenure (YearsAtCompany, YearsInCurrentRole)

Work conditions (OverTime, BusinessTravel)

Target variable: Attrition (Yes/No)

🧠 Feature Engineering

Two engineered features improve interpretability:

TenureBucket → groups employees by years at company.

IncomeBucket → bins monthly income into Low/Mid/High/Very High.

Both are encoded using OneHotEncoder for model compatibility.

🤖 Model Pipeline

The model uses a ColumnTransformer and Pipeline:

OneHotEncoder for categorical features.

XGBoostClassifier for prediction.

ROC-AUC for performance evaluation.

ROC-AUC: 0.79

This score indicates strong predictive performance.

📈 Visualizations

1️⃣ SHAP Summary Plot

Explains which features most influence attrition predictions.



2️⃣ Attrition by Department

Shows turnover patterns across departments.



3️⃣ Attrition by Tenure

Highlights attrition trends by employee tenure.



🔍 Key Insights

Employees working OverTime are more likely to leave.

Higher MonthlyIncome and StockOptionLevel reduce attrition.

Frequent BusinessTravel increases attrition risk.

Low JobSatisfaction and EnvironmentSatisfaction strongly predict attrition.

Short-tenure employees (0–2 years) show higher turnover.

🚀 How to Run

Install dependencies:

pip install -r requirements.txt

Run the analysis:

python notebooks/attrition_analysis.py

💡 Future Improvements

Add model comparison (RandomForest, Logistic Regression).

Build a Streamlit dashboard for interactive exploration.

Deploy via FastAPI for real-time predictions.

👤 Author

Kaden Davis - Lexington, KY, Focused on data analytics, SAP systems, and predictive modeling.

🧩 Business Impact

This project helps HR teams proactively identify employees at risk of leaving, enabling targeted retention strategies and improved workforce planning.