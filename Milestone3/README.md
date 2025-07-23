# 📌 Appendix: Milestone 3 - E-commerce Review Analysis System

## **Overview**
Milestone 3 focuses on customer review analysis in the **E-commerce** domain. It integrates **Together AI** embeddings for semantic representation, **Pinecone** for vector storage and retrieval, and **Streamlit** for a smooth interactive interface. The goal is to collect, store, and analyze customer feedback and provide actionable insights to business managers.

---

## **Customer Review Submission UI**

- **Built With**: `Streamlit`
- **Features**:
  - Customers can submit product reviews in real-time via a simple web form.
  - Rating slider to rate products (1–10).
  - Review is assigned a unique ID and timestamp.
- **Sentiment Analysis**:
  - Uses `TextBlob` to determine sentiment polarity of each review.
  - Sentiment score is saved alongside the review data.

- **Embedding & Vector Storage**:
  - Uses Together AI (`m2-bert-80M-32k-retrieval`) to generate review embeddings.
  - Vectors are stored in a Pinecone index for future semantic search and retrieval.

- **Storage**:
  - Review entries are saved in `reviews_data.xlsx`.
  - Metadata and embeddings are upserted to Pinecone.

---

## **Manager Review Analysis UI**

- **Built With**: `Streamlit`
- **Key Functionalities**:
  - **Query Input**: Managers can enter queries (e.g., "packaging problem", "fast delivery").
  - **Relevant Review Retrieval**: SentenceTransformer encodes the query; Pinecone returns top-k similar reviews.
  - **Summarization**: Retrieved reviews are combined and displayed as bullet points.
  - **Word Cloud**: Visual representation of frequently used words in matched reviews.
  - **Download Option**: Summary can be downloaded as a `.txt` report.

---

## **Final Outcomes**

✅ Seamless submission of reviews with sentiment scores and timestamps  
✅ Efficient semantic search using Pinecone vector index  
✅ User-friendly dashboards for both customers and managers  
✅ AI-powered summarization of customer sentiments  
✅ Visual insights through word clouds and downloadable summaries

---

## **UI Outcomes Images**

### **Customer Review Submission UI**
![sentiment]()
![sentiment2]()
![sentiment3]()
![sentiment4]()

### **Manager Review Analysis UI**
![manager1]()
![manager2]()

---

