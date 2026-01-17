# 📉 Customer Churn Prediction using Machine Learning

## 📌 Project Overview

Customer churn refers to customers who stop using a company’s services.
This project focuses on predicting whether a customer is likely to churn based on their demographics, services subscribed, account information, and billing details using Machine Learning classification techniques.

The project demonstrates a complete end-to-end ML workflow including data analysis, preprocessing, model training, evaluation, model saving, and deployment using a Streamlit dashboard.

---

## 🎯 Objective

* Predict customer churn (Yes / No)
* Identify high-risk customers
* Support data-driven customer retention strategies

---

## 📂 Dataset

* Dataset: Telco Customer Churn Dataset
* Rows: 7,043
* Columns: 50
* Target Variable: Churn Label

Important Note:
Columns causing data leakage such as Churn Reason, Churn Score, and Customer Status were removed before training the model.

---

## 🛠️ Technologies Used

### Programming & Libraries

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Joblib
* Streamlit

### Machine Learning

* Logistic Regression
* StandardScaler
* Label Encoding

---

## 📊 Exploratory Data Analysis (EDA)

Key insights obtained from EDA:

* Customers with shorter tenure are more likely to churn
* Month-to-month contracts show higher churn rates
* Higher monthly charges are associated with higher churn
* Long-term contracts reduce churn probability

---

## ⚙️ Project Workflow

1. Data Loading and Inspection
2. Data Cleaning and Missing Value Handling
3. Exploratory Data Analysis
4. Feature Encoding and Scaling
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Model Saving (Dumping)
9. Streamlit Dashboard Development

---

## 📈 Model Evaluation

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

Recall was emphasized because missing a churn customer is costly for businesses.

---

## 💾 Model Deployment

The trained model and preprocessing objects were saved using Joblib:

* churn_model.pkl
* scaler.pkl
* model_columns.pkl

These files are loaded into the Streamlit application for real-time predictions.

---

## 🖥️ Streamlit Dashboard

Dashboard features include:

* Interactive customer input
* Real-time churn prediction
* Churn probability display
* Simple and user-friendly interface

### Run the Application

```
streamlit run app.py
```

---

## 🚀 Future Enhancements

* Use Random Forest or XGBoost models
* Apply One-Hot Encoding for categorical variables
* Add feature importance visualization
* Enable CSV file upload in Streamlit
* Deploy the application on Streamlit Cloud or Hugging Face

---

## 👤 Author

Savan Patel


---

## ⭐ Conclusion

This project demonstrates a complete machine learning lifecycle from raw data to deployment. It is suitable for academic submission, portfolio presentation, and interview discussions.

If you find this project useful, feel free to star the repository.
