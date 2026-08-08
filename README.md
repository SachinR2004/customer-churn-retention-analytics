Customer Churn & Retention Analytics

Project Overview

Customer churn is a major business challenge for subscription-based companies. Identifying customers who are likely to leave allows businesses to take proactive retention measures before churn occurs.

This project develops a complete customer churn analytics pipeline:

- Exploratory Data Analysis (EDA)
- Data preprocessing
- Feature engineering
- Logistic Regression model development
- Model evaluation
- Classification threshold selection
- Individual customer churn prediction
- Interactive Streamlit dashboard
- Business-oriented retention recommendations

Exploratory Data Analysis

The analysis examines customer churn from multiple perspectives, including:

- Overall churn distribution
- Customer tenure
- Contract type
- Monthly charges
- Total charges
- Internet and service usage
- Customer demographics
- Service adoption
- Relationships between customer characteristics and churn

Model Performance

| Metric                   |      Score |
| ------------------------ | ---------: |
| Accuracy                 | **77.86%** |
| Precision                | **57.08%** |
| Recall                   | **66.84%** |
| F1 Score                 | **61.58%** |
| ROC-AUC                  | **0.8423** |
| Classification Threshold |   **0.40** |


Project Structure
customer-churn-retention-analytics/
│
├── app.py
├── dashboard.py
├── prediction.py
├── insights.py
├── style.css
├── requirements.txt
├── README.md
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│   └── customer_churn_analysis.ipynb
│
└── screenshots/
    ├── dashboard.png
    ├── prediction.png
    └── insights.png


    Tech Stack
Programming
 - Python
Data Analysis
- Pandas
- NumPy
Machine Learning
- Scikit-learn
- Logistic Regression
Classification metrics
- Probability-based classification
Application
- Streamlit
Model Persistence
- Joblib
Frontend Styling
- HTML
- CSS
- Streamlit components



Key Results

The completed project demonstrates an end-to-end machine learning workflow:

Analysed 7,043 customer records
Identified an overall churn rate of approximately 26.54%
Developed a Logistic Regression churn classifier
Achieved 0.8423 ROC-AUC
Achieved 66.84% recall
Selected a 0.40 probability threshold