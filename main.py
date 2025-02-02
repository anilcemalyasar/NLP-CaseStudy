import numpy as np
import pandas as pd
import json
from transformers import BertTokenizer, BertModel
import torch
from sentence_transformers import SentenceTransformer

# JSON dosyasından kitap bilgilerini okuyoruz
try:
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print("JSON verisi başarıyla okundu")
except Exception as e:
    print(f"Hata: {e}")

# Dataframe formatına getiriyoruz
df = pd.DataFrame(data)

# Feature Engineering
df["price"] = df["price"].str.replace("£", "").astype(float)

# EDA ( Exploratory data analysis )
df.head(5)

# Pre-trained BERT modelini embedding vektör yapabilmek için kullanıyoruz
# tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
# model =

m1 = "multi-qa-MiniLM-L6-cos-v1"
sentenceVectorizer1 = SentenceTransformer(m1)
m2 = 'bert-base-nli-mean-tokens'
sentenceVectorizer2 = SentenceTransformer(m2)

# Feature Engineering ( Sentence Embedding vektörleri oluşturacağız )
df["embSentenceTransformer1"] = df["description"].apply(lambda x: sentenceVectorizer1.encode(x))
df["embSentenceTransformer2"] = df["description"].apply(lambda x: sentenceVectorizer2.encode(x))

df[["name", "description", "embSentenceTransformer1", "embSentenceTransformer2"]].head()






