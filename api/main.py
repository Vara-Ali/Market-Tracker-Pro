from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="market_tracker",
        user="postgres",
        password="varaisme"
    )

@app.get("/")
def root():
    return {"message": "Market Tracker API"}

@app.get("/prices")
def get_prices(limit: int = 50):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"SELECT * FROM product_prices ORDER BY timestamp DESC LIMIT %s", (limit,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


@app.get("/prices/source/{source}")
def get_prices_by_source(source: str, limit: int = 50):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT * FROM product_prices
        WHERE source = %s
        ORDER BY timestamp DESC
        LIMIT %s
    """, (source, limit))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data



@app.get("/sources")
def get_sources():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT source FROM product_prices")
    sources = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return {"sources": sources}

@app.get("/prices/search")
def search_products(q: str, limit: int = 50):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    search_term = f"%{q}%"
    cur.execute("""
        SELECT * FROM product_prices
        WHERE LOWER(name) LIKE LOWER(%s)
        ORDER BY timestamp DESC
        LIMIT %s
    """, (search_term, limit))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


@app.get("/prices/history/name/{product_name}")
def get_price_history_by_name(product_name: str, limit: int = 100):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT * FROM product_prices
        WHERE LOWER(name) = LOWER(%s)
        ORDER BY timestamp DESC
        LIMIT %s
    """, (product_name, limit))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
