import streamlit as st
import pandas as pd
import datetime
import random
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_together import TogetherEmbeddings
from textblob import TextBlob

# ✅ Load environment variables
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
PINECONE_HOST = os.getenv("PINECONE_HOST")

# ✅ Set Together API Key
os.environ["TOGETHER_API_KEY"] = TOGETHER_API_KEY

# ✅ Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)
index = pc.Index(host=PINECONE_HOST)

# ✅ Use a supported embedding model
# 👉 Use a working, publicly accessible embedding model
embeddings = TogetherEmbeddings(model="togethercomputer/m2-bert-80M-32k-retrieval")

#embeddings = TogetherEmbeddings(model="BAAI/bge-base-en-v1.5")

# ✅ Define the Excel file
file_name = "reviews_data.xlsx"

# ✅ Load or create DataFrame
if os.path.exists(file_name):
    try:
        df = pd.read_excel(file_name)
    except PermissionError:
        st.error("❌ Please close the 'reviews_data.xlsx' file and try again.")
        st.stop()
else:
    df = pd.DataFrame(columns=["review_id", "customer_id", "review_date", "Review", "Rating", "review_date_numeric"])

# ✅ Helper functions
def generate_id():
    return random.randint(1000, 9999)

def get_sentiment(review_text):
    analysis = TextBlob(review_text)
    return analysis.sentiment.polarity

# ✅ Streamlit UI
st.set_page_config(page_title="E-commerce Review Submission", page_icon="🛍️", layout="centered")
st.title("🛍️ Customer Review Submission")
st.markdown("Share your review about the product! Your feedback helps others. 💬")

# ✅ User inputs
review_text = st.text_area("✍️ Write your review:")
rating = st.slider("⭐ Rate the product (1-10)", 1, 10, 5)
customer_id = st.text_input("🧑‍💼 Customer ID (any identifier):")

# ✅ Submit logic
if st.button("✅ Submit Review", use_container_width=True):
    if review_text.strip() and customer_id.strip():
        new_review_id = generate_id()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        numeric_timestamp = int(datetime.datetime.now().timestamp())
        sentiment_score = get_sentiment(review_text)

        # ✅ Add to DataFrame and save
        new_entry = pd.DataFrame([[new_review_id, customer_id, timestamp, review_text, rating, numeric_timestamp]],
                                 columns=df.columns)
        df = pd.concat([df, new_entry], ignore_index=True)

        try:
            df.to_excel(file_name, index=False)
        except PermissionError:
            st.error("❌ Close 'reviews_data.xlsx' and try again.")
            st.stop()

        # ✅ Store embedding in Pinecone
        review_vector = embeddings.embed_query(review_text)
        index.upsert([
            (str(new_review_id), review_vector, {
                "review_id": new_review_id,
                "customer_id": customer_id,
                "rating": rating
            })
        ])

        # ✅ Output review confirmation
        st.success("✅ Review submitted successfully!")
        st.markdown("### 📌 Submitted Review Details")
        st.write(f"**Review ID:** {new_review_id}")
        st.write(f"**Customer ID:** {customer_id}")
        st.write(f"**Date:** {timestamp}")
        st.write(f"**Review:** {review_text}")
        st.write(f"**Rating:** {rating} ⭐")
        st.write(f"**Sentiment Score:** {sentiment_score:.2f}")

        st.markdown("### 📂 Excel Storage Confirmation")
        st.success("✅ Stored in `reviews_data.xlsx`")

        st.markdown("### 🧠 Pinecone Indexing Confirmation")
        st.success("✅ Vector stored in Pinecone index: `" + PINECONE_INDEX + "`")
    else:
        st.error("❌ Please fill all fields before submitting.")
