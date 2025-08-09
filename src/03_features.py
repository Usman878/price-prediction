import os
import pandas as pd

# Paths
processed_folder = r"C:\Users\umerf\OneDrive\Desktop\New folder (3)\New folder\price-predictor\data\processed"
features_folder = r"C:\Users\umerf\OneDrive\Desktop\New folder (3)\New folder\price-predictor\data\features"

# Create features folder if it doesn't exist
os.makedirs(features_folder, exist_ok=True)

# Loop through processed CSVs and extract features
for file in os.listdir(processed_folder):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(processed_folder, file))

        # EXAMPLE: Create simple numerical features
        # Adjust this part depending on your data
        df['feature_sum'] = df.sum(axis=1, numeric_only=True)
        df['feature_mean'] = df.mean(axis=1, numeric_only=True)

        # Save feature file
        feature_path = os.path.join(features_folder, file)
        df.to_csv(feature_path, index=False)
        print(f"✅ Features saved to: {feature_path}")
