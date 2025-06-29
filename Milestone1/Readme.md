# 📘 Appendix: Milestone 1 – Forecasting Product Demand Using Linear Regression

## 🧠 Introduction
In this milestone, we built a **baseline machine learning model** to predict product-level demand using daily sales data. The model uses structured time-series data, basic feature engineering, and a Linear Regression algorithm to provide foundational insights.

---

## 📊 Data Preparation

We used the **Olist Brazil E-commerce dataset**, particularly:
- `olist_orders_dataset.csv` → contains `order_id`, `purchase timestamp`, and order status.
- `olist_order_items_dataset.csv` → contains `product_id`, `order_id`, and `order_item_id` (used as quantity sold).

### Key Steps:
- Merged order and item data using `order_id`.
- Filtered only `delivered` orders to avoid noise.
- Aggregated total `units_sold` per `product_id` per `date`.

---

## 🛠 Feature Engineering

To capture seasonality and temporal patterns, we extracted:
| Feature   | Description                                |
|-----------|--------------------------------------------|
| `day`     | Day of the month (1–31)                    |
| `month`   | Month of the year (1–12)                   |
| `weekday` | Day of the week (0 = Monday, 6 = Sunday)   |

These were used as input features (`X`) for predicting daily sales (`y`).

---

## 🔗 Data Integration

- Ensured temporal order by sorting by date.
- Selected top 5 selling products and chose 1 for initial modeling.
- Removed unused fields to avoid data leakage.

---

## 🔢 Encoding & Splitting

- No encoding needed — all features were numeric.
- Used an 80/20 **time-aware split** (no shuffling) to train/test the model.

---

## 🤖 Model Training

- Model Used: **Linear Regression** (from scikit-learn)
- Features: `day`, `month`, `weekday`
- Target: `quantity` (daily units sold)

---

## 📈 Evaluation

| Metric     | Value  |
|------------|--------|
| MAE        | 0.95   |
| RMSE       | 1.15   |
| R² Score   | -0.05  |

The model produced a baseline performance but struggled to capture demand spikes. This confirms the need for more advanced modeling in future milestones.

---

## 📊 Visualization

We visualized actual vs predicted sales over the test period:

![Actual vs Predicted Daily Demand](actual_vs_predicted_plot.png)

The chart shows that while the model captures average demand, it underperforms during periods of fluctuation.

---
