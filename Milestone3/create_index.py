from pinecone import Pinecone
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone
pc = Pinecone(api_key=api_key)

# ✅ Create a new 768-dimension index
pc.create_index(
    name="review-index-768",
    dimension=768,
    metric="cosine",
    spec={"serverless": {"cloud": "aws", "region": "us-east-1"}}
)

print("✅ New index 'review-index-768' created.")
