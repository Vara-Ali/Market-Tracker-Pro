import pandas as pd
from sqlalchemy import create_engine

# 🛠️ Replace these with your actual PostgreSQL login details
DB_USER = "postgres"
DB_PASS = "varaisme"   # <-- replace this
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "market_tracker"

def load_data_to_postgres():
    # Load combined CSV
    df = pd.read_csv("data_processing/combined_prices.csv")

    # Create SQLAlchemy engine
    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    # Write to table
    df.to_sql("product_prices", engine, if_exists="append", index=False)
    print(f"✅ Loaded {len(df)} rows into product_prices")

if __name__ == "__main__":
    load_data_to_postgres()
