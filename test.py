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

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
time.sleep(1)

# Get main content div
content_div = driver.find_element(By.XPATH, "//div[@class='content']")

inner_html = content_div.get_attribute("innerHTML")
soup = BeautifulSoup(inner_html, "html.parser")

# Ürün bilgilerini içeren tabloyu bul
product_information_table = soup.find('table', class_="table table-striped")

# Tablodaki tüm satırları al
rows = product_information_table.find_all('tr')

# Bilgileri düzenli bir şekilde almak için bir sözlük oluştur
product_info = {}
for row in rows:
    key = row.find('th').text.strip()
    value = row.find('td').text.strip()
    product_info[key] = value

# import json module
import json

# list of dictionaries of employee data
data = [{"id": ("1", "2", "3"), "name": ("bhanu", "sivanagulu"),
		"department": ("HR", "IT")},
		{"id": ("4", "5", "6"), "name": ("sai", "poori"),
		"department": ("HR", "IT")},
		{"id": ("7", "8", "9"), "name": ("teja", "gowtam"),
		"department": ("finance", "IT")},
		{"id": ("10", "11", "12"), "name": ("sai", "jyothi"),
		"department": ("business", "IT")},
		{"id": ("13", "14", "15"), "name": ("prudhvi", "nagendram"),
		"department": ("business", "IT")}]


# convert into json
final = json.dumps(data, indent=2)

# display
print(final)

print(product_info)


