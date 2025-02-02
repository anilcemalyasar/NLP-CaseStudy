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

# Book Stock Status
book_stock_status_element = soup.find('p', attrs={"class": "instock availability"})
book_stock_status_text = book_stock_status_element.text.strip()
book_stock_status = True if "In Available" in book_stock_status_text else False

match = re.search(r'\((\d+) available\)', book_stock_status_text)
book_stock_amount = 0
if match:
	book_stock_amount = int(match.group(1))
	print(book_stock_amount)

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

data = [
    {
        "name": "A Light in the Attic",
        "price": "£51.77",
        "starRating": "Three",
        "description": "It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love th It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love that Silverstein. Need proof of his genius? RockabyeRockabye baby, in the treetopDon't you know a treetopIs no safe place to rock?And who put you up there,And your cradle, too?Baby, I think someone down here'sGot it in for you. Shel, you never sounded so good. ...more"
    },
    {
        "name": "Tipping the Velvet",
        "price": "£53.74",
        "starRating": "One",
        "description": "\"Erotic and absorbing...Written with starling power.\"--\"The New York Times Book Review \" Nan King, an oyster girl, is captivated by the music hall phenomenon Kitty Butler, a male impersonator extraordinaire treading the boards in Canterbury. Through a friend at the box office, Nan manages to visit all her shows and finally meet her heroine. Soon after, she becomes Kitty's \"Erotic and absorbing...Written with starling power.\"--\"The New York Times Book Review \" Nan King, an oyster girl, is captivated by the music hall phenomenon Kitty Butler, a male impersonator extraordinaire treading the boards in Canterbury. Through a friend at the box office, Nan manages to visit all her shows and finally meet her heroine. Soon after, she becomes Kitty's dresser and the two head for the bright lights of Leicester Square where they begin a glittering career as music-hall stars in an all-singing and dancing double act. At the same time, behind closed doors, they admit their attraction to each other and their affair begins. ...more"
    },
    {
        "name": "Soumission",
        "price": "£50.10",
        "starRating": "One",
        "description": "Dans une France assez proche de la nôtre, un homme s’engage dans la carrière universitaire. Peu motivé par l’enseignement, il s’attend à une vie ennuyeuse mais calme, protégée des grands drames historiques. Cependant les forces en jeu dans le pays ont fissuré le système politique jusqu’à provoquer son effondrement. Cette implosion sans soubresauts, sans vraie révolution, s Dans une France assez proche de la nôtre, un homme s’engage dans la carrière universitaire. Peu motivé par l’enseignement, il s’attend à une vie ennuyeuse mais calme, protégée des grands drames historiques. Cependant les forces en jeu dans le pays ont fissuré le système politique jusqu’à provoquer son effondrement. Cette implosion sans soubresauts, sans vraie révolution, se développe comme un mauvais rêve.Le talent de l’auteur, sa force visionnaire nous entraînent sur un terrain ambigu et glissant ; son regard sur notre civilisation vieillissante fait coexister dans ce roman les intuitions poétiques, les effets comiques, une mélancolie fataliste.Ce livre est une saisissante fable politique et morale. ...more"
    }
]

documents = [d["description"] for d in data]

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Create an instance of CountVectorizer
vectorizer = CountVectorizer()

# Fit the vectorizer to the documents and transform the documents into a document-term matrix
X = vectorizer.fit_transform(documents)

# Get the feature names (tokens)
feature_names = vectorizer.get_feature_names_out()

# Print the feature names
print(feature_names)

# Print the document-term matrix
# print(X.toarray())

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(documents)

print(X.shape)  # (örnek sayısı, kelime sayısı)

from sklearn.metrics.pairwise import cosine_similarity

# Cosine similarity matrisini hesapla
similarity_matrix = cosine_similarity(X)

# Benzerlik matrisini görüntüle
print(similarity_matrix)


