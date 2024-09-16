import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Launching Chrome Browser...")

    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        service=Service(chrome_driver_path),
        options=options,
    )

    try:
        driver.get(website)
        print("Waiting for the page to load...")
        time.sleep(10)
        print("Page loaded. Scraping data...")
        html = driver.page_source
        print("Scraping complete!")
        return html
    finally:
        driver.quit()