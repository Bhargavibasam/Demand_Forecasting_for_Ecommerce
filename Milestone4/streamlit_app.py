import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from prophet import Prophet
from pymongo import MongoClient
import joblib
import sys, os

# Configure matplotlib for Streamlit
plt.rcParams.update({'figure.max_open_warning': 0})

# Add milestone2 path
sys.path.append(os.path.join(os.path.dirname(__file__), "milestone2"))
import prepare_model_input


# --- Dashboard Tab ---
def run_dashboard():
    import random
    st.info("Predictions will be generated using pre-processed milestone2 features.")
    X = prepare_model_input.prepare_input()
    # Mock prediction (no model needed)
    categories = ["electronics", "toys", "clothing", "books"]
    X['Predicted_Category'] = [random.choice(categories) for _ in range(len(X))]

    st.write("Predictions generated:")
    st.write(X.head(10))

    st.download_button(
        label="Download Predictions",
        data=X.to_csv(index=False).encode('utf-8'),
        file_name='predictions.csv',
        mime='text/csv'
    )


# --- Forecasting Tab ---
def run_forecasting():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["demand_forecasting_db"]
    collection = db["forecasts"]

    st.title("Demand Forecasting")

    # Load milestone1 datasets
    orders = pd.read_csv("milestone1/olist_orders_dataset.csv", parse_dates=['order_purchase_timestamp'])
    items = pd.read_csv("milestone1/olist_order_items_dataset.csv")
    products = pd.read_csv("milestone1/olist_products_dataset.csv")

    merged = items.merge(orders, on="order_id", how="left")
    merged = merged.merge(products, on="product_id", how="left")

    df = merged[['order_purchase_timestamp', 'product_category_name']].dropna()
    daily = (
        df.groupby([df['order_purchase_timestamp'].dt.date, 'product_category_name'])
        .size()
        .reset_index(name='demand')
    )
    daily.rename(columns={'order_purchase_timestamp': 'date'}, inplace=True)
    daily['date'] = pd.to_datetime(daily['date'])

    # Category selector
    categories = sorted(daily['product_category_name'].unique())
    category = st.selectbox("Select Product Category", categories)
    months = st.slider("Months to forecast", 1, 6, 3)

    # Filter for category
    cat_data = daily[daily['product_category_name'] == category]
    cat_data = cat_data.groupby('date')['demand'].sum().reset_index()

    # Load Prophet model
    with open("milestone4/prophet_model.pkl", "rb") as f:
        model_prophet = pickle.load(f)

    # Forecast
    future = model_prophet.make_future_dataframe(periods=30 * months)
    forecast = model_prophet.predict(future)

    # Plot forecast
    st.subheader(f"Forecast for {category} (next {months} months)")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(cat_data['date'], cat_data['demand'], label="Historical")
    ax.plot(forecast['ds'], forecast['yhat'], label="Forecast")
    ax.fill_between(
        forecast['ds'],
        forecast['yhat_lower'],
        forecast['yhat_upper'],
        color='lightblue', alpha=0.3, label="Confidence interval"
    )
    ax.legend()
    st.pyplot(fig)

    # Save results to MongoDB
    forecast_json = forecast.to_dict(orient="records")
    record = {
        "category": category,
        "months": months,
        "forecast_results": forecast_json
    }
    collection.insert_one(record)
    st.success(f"Forecast results saved to MongoDB for category '{category}'.")


# --- Sidebar navigation ---
st.sidebar.title("Demand Forecasting App")
option = st.sidebar.radio("Go to", ("Dashboard","Forecasting"))

if option == "Dashboard":
    run_dashboard()

elif option == "Forecasting":
    run_forecasting()
