import joblib

# Load your model
model = joblib.load("xgb_model_category.pkl")

# Print the features it expects
print(model.get_booster().feature_names)
