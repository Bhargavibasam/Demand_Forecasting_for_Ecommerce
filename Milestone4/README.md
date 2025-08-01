# 📌Milestone 4 – Final Integration & Advanced Forecasting

## **Overview**
Milestone 4 marks the **final stage** of the E-commerce Demand Forecasting project.  
This milestone integrates:
- **Mock Predictions** (Dashboard)  
- **Advanced Forecasting** using **Prophet** (trained offline)

The final application is a **Streamlit app** with only two modules:
1. **Dashboard** – Mock product category predictions using preprocessed Milestone 2 features.
2. **Forecasting** – Advanced time-series forecasting using a trained Prophet model.

---

## **Key Components**

### **1. Dashboard (Mock Predictions)**
- Uses **Milestone 2 feature files**.
- Generates **mock predictions** for product categories:
  - Categories: `electronics`, `toys`, `clothing`, `books`
- Allows download of predictions as a CSV file.

---

### **2. Advanced Forecasting**
- **Datasets** from Milestone 1:
  - `olist_orders_dataset.csv`
  - `olist_order_items_dataset.csv`
  - `olist_products_dataset.csv`
- **Prophet model**:
  - Trained offline using `advanced_forecasting.py`.
  - Saved as `prophet_model.pkl`.
- **Forecasting process**:
  - Choose a product category.
  - Forecast demand for the next **1 to 6 months**.
  - Display results with a line plot (historical vs forecast).
  - Save results to MongoDB.

---

## **Files in Milestone 4**

- `streamlit_app.py` – Final app with two sections (Dashboard & Forecasting)
- `advanced_forecasting.py` – Script to train and save Prophet model
- `prophet_model.pkl` – Pre-trained forecasting model
- `appendix.md` – This documentation file

---

## **Final Outcomes**
- **Simplified Dashboard**: Mock predictions for user-friendliness  
- **Advanced Forecasting**: Time-series forecasting with Prophet  
- **Streamlined UI**: Only two tabs for clarity  
- **MongoDB Integration**: Stores forecast results automatically  

---
## **Output Images**
### Advacnce Forecating Images
### Data Stored Images
### DashPrediction Images



