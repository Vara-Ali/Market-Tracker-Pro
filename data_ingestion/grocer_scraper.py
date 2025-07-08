from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime
import time

def setup_driver():
    options = Options()
    # Comment for debugging if needed
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--ignore-certificate-errors")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_grocer():
    url = "https://grocerapp.pk/fruits-and-vegetables/"
    driver = setup_driver()
    driver.get(url)
    time.sleep(5)

    # Scroll to load all products
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # 1. Get product names from img alt
    img_elements = driver.find_elements(By.CSS_SELECTOR, "img.MuiCardMedia-img")
    names = [img.get_attribute("alt").strip() for img in img_elements if img.get_attribute("alt")]

    # 2. Get prices
    price_elements = driver.find_elements(By.CSS_SELECTOR, "h6.MuiTypography-subtitle2")
    prices = [price.text.strip() for price in price_elements if "Rs." in price.text]

    # 3. Zip and clean
    products = []
    for name, price in zip(names, prices):
        products.append({
            "name": name,
            "price": price,
            "source": "GrocerApp",
            "timestamp": datetime.now().isoformat()
        })

    print(f"✅ Found {len(products)} product entries")

    df = pd.DataFrame(products)
    df.to_csv("grocer_prices.csv", index=False)
    print("✅ Scraped and saved GrocerApp data")

    driver.quit()

if __name__ == "__main__":
    scrape_grocer()
