# Demand Forecasting for E-commerce

## Project Overview
This project builds an **AI/ML-powered demand forecasting and customer insights system** for the e-commerce domain.  
The system uses:
- **Time-series forecasting** (Prophet) to predict future demand,
- **Customer reviews analysis** (NLP with Together AI + Pinecone),
- And an **interactive Streamlit dashboard** to integrate insights into a single platform.

By combining **demand prediction, forecasting, and sentiment analysis**, this project empowers businesses to plan inventory, optimize product categories, and monitor customer opinions in real time.

---

## Key Outcomes
- **Accurate demand forecasting** for e-commerce product categories.
- **Customer insights** via semantic search and sentiment monitoring.
- **Interactive dashboards** for predictions, trend visualization, and feedback analysis.
- **Real-time storage** of forecasts into MongoDB for data-driven decision-making.

---

## Repository Structure & Milestones
The project is divided into **four milestones**, each building upon the previous to achieve the final application.

---

### **Milestone 1: Data Preparation & Baseline Demand Prediction**

**Objective:**  
Clean and process the **Olist e-commerce dataset**, build a baseline model to predict future product demand.

**Key Steps:**
1. **Data Preparation**  
   - Merged datasets (orders, products, items).  
   - Performed missing value handling and basic cleaning.

2. **Feature Engineering**  
   - Created time-based features such as month, day, week of purchase.  

3. **Baseline Model**  
   - Built a **Linear Regression model** using cleaned features.
   - Evaluation metrics: **MAE, RMSE, R²**

**Outcome:**  
A basic model that can predict sales demand trends, providing a foundation for advanced modeling.

---

### **Milestone 2: Feature Engineering & Dashboard Development**

**Objective:**  
Move towards a **more structured feature pipeline** and provide a **Streamlit dashboard for predictions**.

**Key Steps:**
1. **Feature Files Creation**  
   - Generated `.xlsx` files such as:
     - `location_features.xlsx`
     - `behavior_features.xlsx`

2. **Streamlit Dashboard (Predictions Module)**  
   - Initially designed to use machine learning encoders, but later simplified with **mock predictions** to avoid model complexity.
   - Shows predictions table and download button.

**Outcome:**  
An easy-to-use **dashboard** that predicts recommended product categories (mock predictions) based on preprocessed features.

---

### **Milestone 3: Customer Review Analysis System**

**Objective:**  
Implement a **review submission and analysis system** to extract insights from customer feedback.

**Key Steps:**
1. **Customer Review Submission**  
   - UI built with Streamlit.
   - Customers submit reviews with a rating slider (1–10).
   - Sentiment analysis performed using **TextBlob**.
   - Reviews saved into `reviews_data.xlsx`.

2. **Embeddings & Vector Database**  
   - Review embeddings generated using **Together AI (m2-bert)**.
   - Stored in **Pinecone** for semantic search.

3. **Manager Analysis Dashboard**  
   - Query input to retrieve semantically relevant reviews.
   - Summarization of retrieved reviews.
   - Word cloud visualization.
   - Option to download summaries.

**Outcome:**  
- Enables semantic search and sentiment insights from customer reviews.
- Provides a **review-driven decision support tool**.

---

### **Milestone 4: Advanced Forecasting & Final App Integration**

**Objective:**  
Enhance forecasting with **Prophet** and finalize the integrated dashboard.

**Key Steps:**
1. **Advanced Forecasting**  
   - Implemented **Prophet model** for category-wise demand forecasting for upcoming months.
   - Integrated interactive controls: select category and months to forecast.
   - Visualization includes confidence intervals.

2. **MongoDB Integration**  
   - Forecast results automatically saved to MongoDB for future analysis.

3. **Final Streamlit App Integration**  
   - Final app contains two main sections:
     1. **Dashboard** – Predictions (mock)
     2. **Forecasting** – Advanced forecasting
   - Reviews module is available in milestone 3 and not repeated in the final app.

**Outcome:**  
A **fully functional dashboard** combining demand predictions and advanced forecasting in a user-friendly interface.

---

## Final Outcomes
- **Streamlined, business-ready application** combining data insights and demand forecasting.
- **Improved planning** through advanced forecasting.
- **Customer-driven analytics** with semantic search for reviews.
- **Integration with MongoDB and Pinecone** for scalable storage and vector retrieval.

---
## Future Enhancements

In the future, this project can be improved with:

- **Real predictions:** Replace mock random predictions with a proper trained ML model.
- **Better forecasting:** Use deep learning models (LSTM/GRU) along with Prophet for more accurate demand forecasting.
- **Deployment:** Deploy the app on cloud platforms like AWS or Streamlit Cloud for easy access.
- **Multi-language support:** Handle customer reviews in different languages.

---

## Setup Instructions:

 Clone the repository:
```bash
git clone https://github.com/Bhargavibasam/Demand_Forecasting_for_Ecommerce.git
cd Demand_Forecasting_for_Ecommerce
