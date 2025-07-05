import pandas as pd

# Step 1: Load base file (customer IDs and basic info)
base_df = pd.read_excel("03_customer_features.xlsx")

# Step 2: List of all remaining feature files to merge
merge_files = [
    "04_customer_behaviour_features.xlsx",
    "05_customer_recency_features.xlsx",
    "06_location_features.xlsx",
    "07_age_features.xlsx"
]

# Step 3: Merge all features using 'customer_id'
for file in merge_files:
    df_part = pd.read_excel(file)
    if 'customer_id' in df_part.columns:
        base_df = pd.merge(base_df, df_part, on="customer_id", how="outer")
    else:
        print(f"❌ Skipped {file}: 'customer_id' not found.")

# Step 4: Save merged features
base_df.to_excel("final_merged_features.xlsx", index=False)
print("✅ final_merged_features.xlsx created.")

# Step 5: Create features.xlsx template for model compatibility
pd.DataFrame(base_df.columns).to_excel("features.xlsx", index=False, header=False)
print("✅ features.xlsx (model input feature list) created.")
