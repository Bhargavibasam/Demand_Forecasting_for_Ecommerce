import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from pymongo import MongoClient

# --- MongoDB Setup ---
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_db"]
collection = db["category_predictions"]

# --- Email Notification Function ---
def send_email(name, email, categories, customer_id):
    sender_email = "22nnia0566bhargavi@gmail.com"
    sender_password = "xjckxaseqbwflqvv"  # ⚠️ Use app password for security

    subject = "🎉 Your E-commerce Product Recommendations Are Ready!"

    product_list = "\n".join([f"• {cat}" for cat in categories])

    body = f"""Hi {name},

✅ Thank you for using our service!
🧾 Recommendation Report for {name} (Customer ID: {customer_id})
------------------------------------------------------------

📅 Date: {pd.Timestamp.today().strftime('%Y-%m-%d')}

🛍️ Top 3 Recommended Product Categories:
{product_list}

💡 Stay tuned for personalized offers and discounts!

Regards,  
E-commerce AI System  
"""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        st.success("📧 Email with product suggestions sent successfully!")
    except Exception as e:
        st.error(f"⚠️ Failed to send email: {e}")

# --- Streamlit UI ---
st.title("🛍️ E-commerce Product Recommendation System")

name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
customer_id = st.number_input("Enter your Customer ID", min_value=10000, max_value=99999)
location = st.selectbox("Location", ["Bangalore", "Mumbai", "Hyderabad", "Delhi"])
age = st.slider("Your Age", 18, 70)
last_login_days = st.slider("Days since last login", 0, 365)
has_discount_preference = st.radio("Interested in discounts?", ["Yes", "No"])

if st.button("Get My Product Recommendations"):

    input_data = {
        "customer_id": str(int(customer_id)),
        "location": location,
        "age": int(age),
        "last_login_days": int(last_login_days),
        "prefers_discount": 1 if has_discount_preference == "Yes" else 0,
        "email": email
    }
    df = pd.DataFrame([input_data])

    # --- Step 2: Merge Feature Files ---
    merge_files = {
        "07_age_features": "07_age_features.xlsx",
        "03_customer_features": "03_customer_features.xlsx",
        "04_customer_behaviour_features": "04_customer_behaviour_features.xlsx",
        "05_customer_recency_features": "05_customer_recency_features.xlsx",
        "06_location_features": "06_location_features.xlsx"
    }

    for file_key, path in merge_files.items():
        if os.path.exists(path):
            feature_df = pd.read_excel(path)

            if "customer_id" not in feature_df.columns:
                st.error(f"'customer_id' column missing in: {path}")
                st.stop()

            feature_df["customer_id"] = feature_df["customer_id"].astype(str)
            df["customer_id"] = df["customer_id"].astype(str)

            df = df.merge(feature_df, on="customer_id", how="left")
        else:
            st.error(f"📁 Missing feature file: {path}")
            st.stop()

    # --- Step 3: Clean Conflicts like location_x, location_y ---
    if "location_x" in df.columns:
        df.drop(columns=["location_x"], inplace=True)
    if "location_y" in df.columns:
        df.rename(columns={"location_y": "location"}, inplace=True)

    # --- Step 4: Drop Unused Columns ---
    df.drop(columns=["customer_id", "email"], inplace=True, errors='ignore')

    # --- Step 5: Encode Categorical Variables ---
    encoder = joblib.load("encoder.pkl")
    cat_cols = list(encoder.feature_names_in_)
    for col in cat_cols:
        if col not in df.columns:
            df[col] = "Unknown"
    df_encoded = encoder.transform(df[cat_cols])
    encoded_df = pd.DataFrame(df_encoded, columns=encoder.get_feature_names_out())
    df = pd.concat([df.drop(columns=cat_cols), encoded_df], axis=1)

    # --- Step 6: Match with Trained Model Columns ---
    if not os.path.exists("features.xlsx"):
        pd.DataFrame(df.columns).to_excel("features.xlsx", index=False, header=False)
        st.warning("⚠️ 'features.xlsx' created. Please re-run the app.")
        st.stop()

    expected_cols = ['age', 'last_login_days', 'prefers_discount',
                     'location_Bangalore', 'location_Delhi',
                     'location_Hyderabad', 'location_Mumbai']

    for col in expected_cols:
        if col not in df.columns:
            df[col] = 0
    df = df[expected_cols]

    # --- Step 7: Prediction ---
    df = df.select_dtypes(include=[np.number])
    model = joblib.load("xgb_model_category.pkl")
    pred_prob = model.predict_proba(df)
    label_encoder = joblib.load("label_encoder.pkl")
    top_3 = label_encoder.inverse_transform(np.argsort(-pred_prob, axis=1)[0][:3])

    # --- Step 8: Store + Display + Notify ---
    input_data["top_categories"] = list(top_3)
    try:
        collection.insert_one(input_data)
    except Exception as e:
        st.warning(f"⚠️ Failed to save to MongoDB: {e}")

    st.success(f"🎯 Top Recommendations: {', '.join(top_3)}")
    send_email(name, email, top_3, customer_id)
    

    

