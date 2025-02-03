# 📚 NLP-CaseStudy: Kitap Açıklamalarına Göre Benzerlik Analizi

Bu proje, bir kitap koleksiyonunun açıklamalarını analiz eder ve **TF-IDF, CountVectorizer ve BERT Sentence Embeddings** yöntemleri ile kitaplar arasındaki benzerlikleri hesaplar.

## 🚀 Proje Açıklaması
- **TF-IDF, BoW (Bag of Words) ve BERT Embeddings** kullanarak metin vektörleştirme işlemi yapılır.
- **Cosine Similarity** ile kitap açıklamaları arasındaki benzerlik hesaplanır.
- Her kitap için en benzer **5 kitap** belirlenir.
- Sonuçlar **JSON formatında** kaydedilir.

---

## 🛠 Kullanılan Teknolojiler & Bağımlılıklar

Aşağıdaki Python kütüphaneleri gereklidir:

```bash
pip install numpy pandas scikit-learn sentence-transformers
```

- `numpy`: Sayısal işlemler için
- `pandas`: Veri işleme ve analizi için
- `scikit-learn`: TF-IDF, CountVectorizer ve Cosine Similarity hesaplamaları için
- `sentence-transformers`: BERT modeli ile metin embedding'leri oluşturmak için

---

## 📌 Kurulum & Çalıştırma

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

📌 **Benzerlik Analizi Çalıştırma**

![Benzerlik Analizi](path/to/screenshot.png)

📌 **Oluşturulan JSON Çıktısı**

![JSON Çıktı](D:\NLP-CaseStudy-Patika\images\similarities.png)

---

## ✨ Katkıda Bulunma
Eğer projeye katkı sağlamak istiyorsanız, **pull request** gönderebilir veya `issue` açabilirsiniz.

---


