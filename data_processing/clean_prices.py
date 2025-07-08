import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

def clean_price(p):
    try:
        return float(p.replace('Rs.', '').replace(',', '').strip())
    except:
        return None

def clean_name(n):
    return n.split('(')[0].strip().lower()

def clean_product_prices():
    engine = create_engine("postgresql+psycopg2://airflow:airflow@localhost:5432/market_tracker")
    df = pd.read_sql("SELECT * FROM product_prices", con=engine)

    df['clean_price'] = df['price'].apply(clean_price)
    df['clean_name'] = df['name'].apply(clean_name)
    df = df.dropna(subset=['clean_price'])

    df = df[['clean_name', 'clean_price', 'source', 'timestamp']]
    df = df.rename(columns={'clean_name': 'name', 'clean_price': 'price'})

    # Overwrite final cleaned table
    df.to_sql("product_prices_cleaned", con=engine, if_exists='replace', index=False)
    print(f"Cleaned {len(df)} rows and saved to product_prices_cleaned")

if __name__ == "__main__":
    clean_product_prices()
