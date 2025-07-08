# streamlit_app/app.py
import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Market Tracker Pro", layout="wide")

# DB connection (adjust credentials if needed)
@st.cache_resource
def get_connection():
    return psycopg2.connect(
        dbname="market_tracker",
        user="postgres",
        password="varaisme",
        host="localhost",
        port="5432"
    )

conn = get_connection()

# Load product names for dropdown
@st.cache_data
def load_product_names():
    query = "SELECT DISTINCT name FROM product_prices ORDER BY name"
    return pd.read_sql(query, conn)['name'].tolist()

product_names = load_product_names()

# UI
st.title("📈 Market Tracker Pro")
st.subheader("Track Product Prices Over Time")

selected_product = st.selectbox("🔍 Search for a product", product_names)

# Fetch price history
if selected_product:
    query = """
        SELECT price, source, timestamp 
        FROM product_prices 
        WHERE name = %s 
        ORDER BY timestamp DESC
    """
    df = pd.read_sql(query, conn, params=(selected_product,))

    st.write(f"### 📊 Price History for: `{selected_product}`")
    st.dataframe(df, use_container_width=True)

    # Line Chart
    fig = px.line(df, x='timestamp', y='price', color='source',
                  title=f"📉 Price Trend - {selected_product}")
    st.plotly_chart(fig, use_container_width=True)
