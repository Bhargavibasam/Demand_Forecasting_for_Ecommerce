# 🛍️ Milestone 2: Personalized Product Category Recommendation System

## Introduction

This milestone builds a real-time product category recommendation system for an e-commerce platform. It uses machine learning to predict the top 3 categories a customer is most likely to purchase based on demographic, location, and behavioral features. The system includes:

- A Streamlit-based web interface
- Feature merging and preprocessing pipeline
- XGBoost-based recommendation engine
- MongoDB for storing customer activity
- Email notifications for product recommendations

---

## System Architecture

### 🔷 Components:
- **User Input Form**: Takes customer ID, name, email, location, age, login behavior, and discount interest.
- **Feature Engineering**: Merges `.xlsx` feature files generated in Milestone 1.
- **ML Model Integration**: Loads pre-trained XGBoost model and label encoder to output top 3 categories.
- **Email Notification**: Sends an email with personalized category suggestions.
- **MongoDB Storage**: Logs the input and predictions in `ecommerce_db.category_predictions`.

---

## Functional Implementation

### 1️⃣ User Input

Customers enter:

- Name and email  
- Age and location  
- Days since last login  
- Discount preference  
- Customer ID (linked with feature files)

---

### 2️⃣ Feature Merging & Transformation

- Joins the following `.xlsx` files using `customer_id`:
  - `03_customer_features.xlsx`
  - `04_customer_behaviour_features.xlsx`
  - `05_customer_recency_features.xlsx`
  - `06_location_features.xlsx`
  - `07_age_features.xlsx`
- Cleans column conflicts (e.g., `location_x`, `location_y`)
- One-hot encodes categorical values using a pre-trained encoder
- Matches model input structure using `features.xlsx`

---

### 3️⃣ Model Prediction

- Uses `xgb_model_category.pkl` to predict probabilities of categories
- Retrieves top 3 with highest probability
- Converts encoded labels using `label_encoder.pkl`

---

### 4️⃣ Email Notification

- Sends an email with predicted categories using Gmail SMTP
- Uses App Password authentication (configured once)
- Message content is clean and personalized

---

### 5️⃣ MongoDB Logging

- Saves each submission to local MongoDB `ecommerce_db.category_predictions` collection
- Enables future analytics and audit

---

## Sample Output

🎯 Top Recommendations:
