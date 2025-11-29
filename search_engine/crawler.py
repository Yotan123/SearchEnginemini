import os
import requests
from bs4 import BeautifulSoup

class WebCrawler:
    def __init__(self, urls_file="search_engine/urls.txt", save_path="search_engine/dataset"):
        self.urls_file = urls_file
        self.save_path = save_path
        os.makedirs(self.save_path, exist_ok=True)

    def load_urls(self):
        """Membaca daftar URL dari urls.txt"""
        with open(self.urls_file, "r", encoding="utf-8") as file:
            urls = [line.strip() for line in file if line.strip()]
        return urls

    def crawl_url(self, url, idx):
        """Mengambil konten dari satu URL"""
        try:
            print(f"[CRAWLING] {url}")
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            text = soup.get_text(separator=" ", strip=True)

            filename = f"page_{idx}.txt"
            filepath = os.path.join(self.save_path, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"[SAVED] {filepath}")
        except Exception as e:
            print(f"[ERROR] {url} → {e}")

    def crawl(self):
        """Menjalankan crawling semua URL"""
        urls = self.load_urls()
        for idx, url in enumerate(urls):
            self.crawl_url(url, idx)

if __name__ == "__main__":
    crawler = WebCrawler()
    crawler.crawl()
