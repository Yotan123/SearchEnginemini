# Search Engine Sederhana 🔍

Proyek ini adalah tugas kuliah untuk membuat mesin pencari sederhana. Sistem ini melakukan *crawling* data artikel berita, melakukan *indexing*, dan memungkinkan pengguna mencari berita berdasarkan kata kunci.

## 🚀 Fitur
- **Crawling:** Mengambil data judul dan isi berita dari website target otomatis.
- **Indexing:** Menyimpan data teks ke dalam database agar mudah dicari.
- **Searching:** Mencari berita yang relevan berdasarkan query pengguna.

## 🛠️ Teknologi yang Digunakan
- **Bahasa:** Python
- **Database:** FIle TZT (Plain Text)
- **Library:** - `BeautifulSoup` (untuk crawling)
               - `Flask` (Web Framework)
  

## 📂 Cara Menjalankan
1. Clone repository ini:
   ```bash
   git clone [https://github.com/Yotan123/SearchEnginemini.git](https://github.com/Yotan123/SearchEnginemini.git)

2. Install Dependencies
    ```bash
    pip install -r requirements.txt


Cara Menggunakan 
1. Masukkan daftar url kedalam file urls.txt
2. Jalankan Web Crawler:
    ```bash
    python search_engine/crawler.py

    Hasil Crawling akan masuk kedalam folder search_engine/dataset/
3. Jalankan Search Engine Website
     ```bash
    python app.py
4. lalu buka url yang diberikan program nya seperti ini 
    ```bash 
    http://127.0.0.1:5000