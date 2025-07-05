import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import joblib

# Define the categorical columns used in your project
categorical_cols = ['location']

# Create dummy data to fit the encoder
dummy_data = pd.DataFrame({
    'location': ['Bangalore', 'Mumbai', 'Hyderabad', 'Delhi']
})

# Create and fit OneHotEncoder
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoder.fit(dummy_data[categorical_cols])

# Save the encoder
joblib.dump(encoder, "encoder.pkl")
print("✅ encoder.pkl created successfully.")
