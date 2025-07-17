# ------------------------------
# manager_review_analysis.py
# ------------------------------
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from io import BytesIO

# Load API keys from .env
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_HOST = os.getenv("PINECONE_HOST")

# Init Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(host=PINECONE_HOST)

# Load SentenceTransformer model
model = SentenceTransformer("all-mpnet-base-v2")  # ✅ 768-dim


# Load review data
@st.cache_data
def load_data():
    return pd.read_excel("reviews_data.xlsx")

df = load_data()

# Streamlit UI
st.title(" Manager's Review Analysis Tool")
query = st.text_input("Ask a question about customer reviews")

if st.button("Get Insights") and query:
    query_vector = model.encode(query).tolist()
    results = index.query(vector=query_vector, top_k=5, include_metadata=True)

    matched_ids = [int(match.metadata["review_id"]) for match in results.matches]
    req_df = df[df["review_id"].isin(matched_ids)]

    if not req_df.empty:
        reviews_combined = " ".join(req_df["Review"].tolist())

        # Simple summary method (fallback)
        summary = "\n\n".join([f"• {rev}" for rev in req_df["Review"].tolist()])

        st.subheader("💡 Summary")
        st.write(summary)

        output = BytesIO()
        output.write(summary.encode())
        st.download_button("📥 Download Summary", data=output, file_name="summary.txt", mime="text/plain")

        words = WordCloud(width=300, height=200, background_color="white").generate(reviews_combined)
        st.sidebar.subheader("🌟 Word Cloud")
        st.sidebar.image(words.to_array())
    else:
        st.warning("No matching reviews found for this query.")
