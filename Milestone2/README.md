# 🛍️ Milestone 2: Personalized Product Category Recommendation System

## 📌 Objective

To develop an intelligent e-commerce system that recommends the **top 3 product categories** to users based on their demographics, browsing behavior, and location. The project uses a trained ML model, a user-friendly Streamlit interface, MongoDB for storage, and email notifications to enhance the customer experience.

---

## 💡 Features Implemented

### 1. **Streamlit Web Interface**

* Collects user input including:

  * Name
  * Email
  * Customer ID
  * Age
  * Location (select from dropdown)
  * Last login days
  * Discount preference

### 2. **Feature Merging**

* Combines customer information with preprocessed `.xlsx` files:

  * `03_customer_features.xlsx`
  * `04_customer_behaviour_features.xlsx`
  * `05_customer_recency_features.xlsx`
  * `06_location_features.xlsx`
  * `07_age_features.xlsx`
* Merging is performed using `customer_id`.
* Conflict resolution for duplicated `location` columns.

### 3. **Preprocessing & Encoding**

* Loads a `OneHotEncoder` from `encoder.pkl` to encode categorical columns.
* Adds missing model columns and ensures the correct order using `features.xlsx`.

### 4. **Prediction using XGBoost**

* Uses a trained `xgb_model_category.pkl` to predict product category probabilities.
* Converts numerical labels to category names using `label_encoder.pkl`.
* Selects the top 3 recommended product categories.

### 5. **Email Notification**

* Sends an automated email using Gmail SMTP.
* Content includes:

  * User name
  * List of 3 recommended categories
  * Personalized message

### 6. **MongoDB Storage**

* Connects to a local MongoDB database `ecommerce_db`.
* Stores input data and predicted categories into the `category_predictions` collection.

---

## 🔧 How to Run

### Prerequisites

* Python 3.10+
* Required libraries: pandas, numpy, joblib, streamlit, pymongo, xgboost, scikit-learn
* MongoDB installed and running (`mongod`)
* MongoDB Compass installed (optional)
* Gmail App Password setup for sending email

### Run the App

```bash
streamlit run ecommerce_predictor.py
```
---
## ✅ Conclusion

This milestone successfully integrated:

* Real-time data input
* Model-based recommendation logic
* Email delivery system
* NoSQL database for historical storage

The system offers both functional accuracy and user-friendliness, representing a solid step toward a deployable e-commerce recommendation engine.

---
## 🖼️ Sample Output


