# 04_train.py
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Path to the folder containing all feature CSV files
feature_folder = r"C:\Users\umerf\OneDrive\Desktop\New folder (3)\New folder\price-predictor\data\features"

# Read and combine all CSV files
all_files = [os.path.join(feature_folder, f) for f in os.listdir(feature_folder) if f.endswith(".csv")]
df_list = [pd.read_csv(file) for file in all_files]
df = pd.concat(df_list, ignore_index=True)

print(f"Combined {len(all_files)} feature files into one DataFrame with {df.shape[0]} rows.")

# Assuming 'target' is the column name for the label
X = df.drop(columns=["target"])
y = df["target"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
model_path = r"C:\Users\umerf\OneDrive\Desktop\New folder (3)\New folder\price-predictor\models\linear_model.pkl"
os.makedirs(os.path.dirname(model_path), exist_ok=True)
joblib.dump(model, model_path)

print(f"Model saved to {model_path}")
print(f"Training score: {model.score(X_train, y_train):.4f}")
print(f"Test score: {model.score(X_test, y_test):.4f}")
