from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import re
import numpy as np
import json
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

def get_book_urls(driver, url, max_pagination):
    book_elements_xpath = "//div[@class = 'image_container']//a"
    book_urls = []

    for i in range(1, max_pagination + 1):
        update_url = url if url == 1 else url.replace("index", f"catalogue/page-{i}")
        driver.get(update_url)
        time.sleep(SLEEP_TIME)
        book_elements = driver.find_elements(By.XPATH, book_elements_xpath)
        if not book_elements:
            break

        temp_urls = [element.get_attribute("href") for element in book_elements]
        book_urls.extend(temp_urls)

    return book_urls

def get_book_details(driver, url):
    """

    :param driver: WebDriver - Chrome
    :param url: str
    :return: dict
    """

    driver.get(url)
    time.sleep(SLEEP_TIME)

    # Get main content div
    content_div = driver.find_element(By.XPATH, "//div[@class='content']")

    inner_html = content_div.get_attribute("innerHTML")
    soup = BeautifulSoup(inner_html, "html.parser")

    # Book Name
    book_name_element = soup.find('h1')
    book_name = book_name_element.text

    # Book Price
    book_price_element = soup.find('p', attrs={"class": "price_color"})
    book_price = book_price_element.text

    # Book Star Rating
    star_rating_regex = re.compile("^star-rating ")
    book_star_elem = soup.find("p", attrs={"class": star_rating_regex})
    book_star = book_star_elem["class"][-1]

    # Book Description
    desc_element = soup.find('div', attrs={"id": "product_description"})
    book_desc = np.nan
    if desc_element:
        book_desc = desc_element.find_next_sibling().text

    # Book Stock Status
    book_stock_status_element = soup.find('p', attrs={"class": "instock availability"})
    book_stock_status_text = book_stock_status_element.text.strip()
    book_stock_status = True if "In Available" in book_stock_status_text else False

    match = re.search(r'\((\d+) available\)', book_stock_status_text)
    book_stock_amount = 0
    if match:
        book_stock_amount = int(match.group(1))

    json_obj = {
        "name": book_name,
        "price": book_price,
        "starRating": book_star,
        "description": book_desc,
        "stockStatus": book_stock_status,
        "stockAmount": book_stock_amount
    }

    return json_obj

def main():
    driver = initialize_driver()
    page_count = find_page_count(driver, BASE_URL)
    book_urls = get_book_urls(driver, BASE_URL, page_count)

    book_details = []
    for book_url in book_urls:
        book_details.append(get_book_details(driver, book_url))

    with open("data.json", "w", encoding='utf-8') as f:
        json.dump(book_details, f, ensure_ascii=False, indent=4)

    # print(len(book_urls))

if __name__ == "__main__":
    main()

