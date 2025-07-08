from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime
import time

def scrape_metro_with_selenium():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-logging")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://www.metro-online.pk/store/fresh-food/fruits-and-vegetables/fresh-vegetables"
    driver.get(url)
    time.sleep(5)  # wait for JS content to load

    # Scroll down to load more products
    SCROLL_PAUSE_TIME = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(30):  # Scroll 5 times — adjust as needed
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


    product_titles = driver.find_elements(By.CLASS_NAME, "CategoryGrid_product_name__3nYsN")
    product_prices = driver.find_elements(By.CLASS_NAME, "CategoryGrid_product_price__Svf8T")

    print(f"Found {len(product_titles)} products")

    data = []
    for title, price in zip(product_titles, product_prices):
        data.append({
            "name": title.text.strip(),
            "price": price.text.strip(),
            "source": "Metro",
            "timestamp": datetime.now().isoformat()
        })

    driver.quit()

    df = pd.DataFrame(data)
    df.to_csv("metro_prices.csv", index=False)
    print("Scraped and saved Metro data")

if __name__ == "__main__":
    scrape_metro_with_selenium()
