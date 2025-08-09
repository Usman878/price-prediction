import os
import pandas as pd

# Absolute path to filenames.txt
filenames_path = r"C:\Users\umerf\OneDrive\Desktop\New folder (3)\New folder\price-predictor\filenames.txt"

# Folder containing raw CSVs
raw_data_folder = r"C:\Users\umerf\OneDrive\Desktop\New folder (3)\New folder\price-predictor\data\raw"

# Folder to save processed CSVs
processed_folder = r"C:\Users\umerf\OneDrive\Desktop\New folder (3)\New folder\price-predictor\data\processed"
os.makedirs(processed_folder, exist_ok=True)

# Read filenames from text file
with open(filenames_path, "r") as f:
    filenames = f.read().splitlines()

print(f"📄 Found {len(filenames)} filenames in filenames.txt")

# Process each file
for file in filenames:
    csv_path = os.path.join(raw_data_folder, file)

    if not os.path.exists(csv_path):
        print(f"❌ File not found: {csv_path}")
        continue

    try:
        df = pd.read_csv(csv_path)

        # Basic preprocessing
        df = df.dropna()               # Remove rows with missing data
        df = df.reset_index(drop=True) # Reset index

        # Save processed file
        output_file = os.path.join(processed_folder, file)
        df.to_csv(output_file, index=False)

        print(f"✅ Processed: {output_file}")

    except Exception as e:
        print(f"⚠️ Error processing {file}: {e}")
