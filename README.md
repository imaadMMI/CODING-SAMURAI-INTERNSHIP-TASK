# 📊 Customer Churn Prediction - Coding Samurai Internship

This repository contains my submission for the **Machine Learning Internship** at **Coding Samurai**. The goal of this project was to build a machine learning model that predicts whether a customer is likely to churn (leave a service) based on behavioral and demographic data.

## 🚀 Project Overview

Customer churn is a critical metric for businesses. By predicting churn, companies can proactively engage at-risk customers. This project involves:
- **Exploratory Data Analysis (EDA)** using Jupyter Notebooks.
- **Preprocessing & Feature Engineering** (Scaling numerical data, encoding categorical variables).
- **Model Training:** Implementing a classification model to predict churn.
- **Deployment:** A user-friendly web interface built with **Streamlit**.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, Joblib
- **Deployment:** Streamlit
- **Environment:** Jupyter Notebook, VS Code

---

## 📂 Project Structure

* `notebook.ipynb`: The complete workflow from data loading to model evaluation.
* `app.py`: The Streamlit web application for real-time predictions.
* `customer_churn_data.csv`: The dataset used for training and testing.
* `model.pkl` & `scaler.pkl`: The saved model and scaler for deployment.
* `learn.md`: Documentation of the learning process during the task.

---

## 🏃‍♂️ How to Run the App

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/imaadMMI/CODING-SAMURAI-INTERNSHIP-TASK.git](https://github.com/imaadMMI/CODING-SAMURAI-INTERNSHIP-TASK.git)
   cd CODING-SAMURAI-INTERNSHIP-TASK
2. **Install dependencies:**
   ```bash
   pip install streamlit joblib scikit-learn pandas numpy
3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py

## How it works

Model & Methodology
The model analyzes four primary features to determine churn probability:

- Age

- Gender (Encoded: Female = 1, Male = 0)

- Monthly Charges

- Tenure (Months stayed with the service)

Workflow:
The input data is first passed through scaler.pkl to ensure the values match the distribution the model was trained on, then fed into the classifier to output a "Churn" or "No Churn" result.


<img width="2048" height="2048" alt="image" src="https://github.com/user-attachments/assets/a9701dfc-64ab-4599-af8a-363cc1a5158a" />


## 📊 Results & Insights
Based on the analysis in notebook.ipynb:

- Tenure Impact: Customers with shorter tenure are significantly more likely to churn, suggesting that early-stage engagement is critical.

- Financial Stress: Higher monthly charges correlate with higher churn rates, indicating price sensitivity among the customer base.

- Accuracy: The classification model provides a robust baseline for identifying at-risk customers, allowing for targeted retention strategies.
