from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import re
import numpy as np
import pandas as pd

# Set constant variables
SLEEP_TIME = 0.25
BASE_URL = "https://books.toscrape.com/index.html"

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options)
    return driver

def find_page_count(driver, url):

    driver.get(url)
    # Sayfa yüklenmesini bekleyelim
    try:
        page_info_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='current']"))
        )
        page_info_text = page_info_element.text  # get_text() yerine .text kullanılmalı
        page_count = int(page_info_text.split("of")[-1].strip())  # trim() yerine strip()
        return page_count
    except Exception as e:
        print("Hata:", e)
        return None

def main():
    driver = initialize_driver()
    page_count = find_page_count(driver, BASE_URL)

if __name__ == "__main__":
    main()

