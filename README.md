# 📚 NLP-CaseStudy: Kitap Açıklamalarına Göre Benzerlik Analizi

Bu proje, bir kitap koleksiyonunun açıklamalarını analiz eder ve **TF-IDF, CountVectorizer ve BERT Sentence Embeddings** yöntemleri ile kitaplar arasındaki benzerlikleri hesaplar.

## 🚀 Proje Açıklaması
- **TF-IDF, BoW (Bag of Words) ve BERT Embeddings** kullanarak metin vektörleştirme işlemi yapılır.
- **Cosine Similarity** ile kitap açıklamaları arasındaki benzerlik hesaplanır.
- Her kitap için en benzer **5 kitap** belirlenir.
- Sonuçlar **JSON formatında** kaydedilir.

---

## 📌 Kurulum & Çalıştırma

## 🛠 Kullanılan Teknolojiler & Bağımlılıklar

Aşağıdaki Python kütüphaneleri gereklidir:

```bash
pip install numpy pandas scikit-learn sentence-transformers selenium beautifulsoup4 torch transformers
```

- `numpy`: Sayısal işlemler için
- `pandas`: Veri işleme ve analizi için
- `scikit-learn`: TF-IDF, CountVectorizer ve Cosine Similarity hesaplamaları için
- `sentence-transformers`: BERT modeli ile metin embedding'leri oluşturmak için
- `selenium`: Web scraping için
- `beautifulsoup4`: HTML verisini ayrıştırmak için
- `torch`: PyTorch tabanlı BERT modelleri için
- `transformers`: Hugging Face Transformer modelleri için

---

## 📌 Kurulum & Çalıştırma
### 🔹 **Yöntem 1: Git reposunu lokalinize klonlayın**
1️⃣ **Projeyi klonlayın:**
```bash
git clone https://github.com/anilcemalyasar/NLP-CaseStudy.git
cd NLP-CaseStudy
```

2️⃣ **Gerekli bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

3️⃣ **Kodunuzu çalıştırın:**
```bash
python book_similarity_analysis.py
```

4️⃣ **Sonuçlar JSON formatında kaydedilir:**
```bash
book_similarity_results.json
```

---

### 🔹 **Yöntem 2: Anaconda ile Virtual Environment Kullanarak**

1️⃣ **Anaconda ile yeni bir sanal ortam oluşturun:**
```bash
conda create --name nlp_env python=3.9
conda activate nlp_env
```

2️⃣ **Gerekli bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

3️⃣ **Kodunuzu çalıştırın:**
```bash
python main.py
```

4️⃣ **Sonuçlar JSON formatında kaydedilir:**
```bash
book_similarity_results.json
```

### 🔹 **Yöntem 3: PyCharm Üzerinden Virtual Environment Kullanarak**

1️⃣ **PyCharm'de yeni bir proje oluşturun ve Virtual Environment seçin.**

2️⃣ **Terminale şu komutları girerek bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

3️⃣ **`main.py` dosyasını çalıştırarak projeyi başlatın.**

4️⃣ **Sonuçlar JSON dosyasında kaydedilecektir.**

---


## 📊 Örnek Çıktı Formatı

JSON dosyası şu formatta olacaktır:
```json
[
  {
    "name": "Kitap 1",
    "tfidf_top5_similar": ["Kitap 2", "Kitap 3", "Kitap 4", "Kitap 5", "Kitap 6"],
    "bow_top5_similar": ["Kitap 7", "Kitap 8", "Kitap 9", "Kitap 10", "Kitap 11"],
    "bert_top5_similar": ["Kitap 12", "Kitap 13", "Kitap 14", "Kitap 15", "Kitap 16"]
  }
]
```

---

## 🖼 Örnek Ekran Görüntüleri

📌 **Web Kazıma ile elde ettiğimiz kitap verileri JSON formatında**

![JSON Kitap Çıktı](https://github.com/anilcemalyasar/NLP-CaseStudy/blob/main/images/books.png)

📌 **Oluşturulan JSON Çıktısı**

![JSON Çıktı](https://github.com/anilcemalyasar/NLP-CaseStudy/blob/main/images/similarities.png)

---



## 📊 Örnek Çıktı Formatı

JSON dosyası şu formatta olacaktır:
```json
[
  {
    "name": "Kitap 1",
    "tfidf_top5_similar": ["Kitap 2", "Kitap 3", "Kitap 4", "Kitap 5", "Kitap 6"],
    "bow_top5_similar": ["Kitap 7", "Kitap 8", "Kitap 9", "Kitap 10", "Kitap 11"],
    "bert_top5_similar": ["Kitap 12", "Kitap 13", "Kitap 14", "Kitap 15", "Kitap 16"]
  }
]
```

## 🌐 Web Scraping ile Veri Kazıma
Bu proje ayrıca **Selenium ve BeautifulSoup** kullanarak kitap verilerini otomatik olarak kazımaktadır.

1️⃣ **Web Scraping kodunu çalıştırmak için:**
```bash
python webscraping.py
```

2️⃣ **Veriler `data.json` dosyasına kaydedilecektir.**

📌 **Web Scraping Programı Code Review:** 
[![Program Code Review Videosu](https://img.youtube.com/vi/SnkLLX9otmU/0.jpg)](https://www.youtube.com/watch?v=SnkLLX9otmU)

📌 **Web Scraping Demo:** 
[![Program Demo Videosu](https://img.youtube.com/vi/1_EsNFBOYpQ/0.jpg)](https://www.youtube.com/watch?v=1_EsNFBOYpQ)

---


