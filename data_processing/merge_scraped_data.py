import pandas as pd
from datetime import datetime
import os

def merge_price_data():
    # Paths
    metro_path = "data_ingestion/metro_prices.csv"
    grocer_path = "data_ingestion/grocer_prices.csv"
    output_path = "data_processing/combined_prices.csv"

    # Load both
    metro = pd.read_csv(metro_path)
    grocer = pd.read_csv(grocer_path)

    # Optional: clean price columns
    for df in [metro, grocer]:
        df["price"] = df["price"].str.replace("Rs.", "", regex=False).str.strip()
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df.dropna(subset=["price"], inplace=True)

    # Combine
    combined = pd.concat([metro, grocer], ignore_index=True)

    # Save to CSV
    os.makedirs("data_processing", exist_ok=True)
    combined.to_csv(output_path, index=False)
    print(f"✅ Combined data saved to {output_path}")
    print(f"🧾 Total entries: {len(combined)}")

if __name__ == "__main__":
    merge_price_data()
