def __init__(self, dataset_folder="dataset"):
    nltk.download("stopwords", quiet=True)
    self.dataset_folder = dataset_folder
    self.docs, self.filenames = self.load_documents()

    if len(self.docs) == 0:
        print("[!] Tidak ada dokumen ditemukan di dataset/. Search engine tetap dijalankan, tapi tidak bisa mencari.")
        self.vectorizer = None
        self.tfidf_matrix = None
        return

    self.vectorizer, self.tfidf_matrix = self.build_tfidf()
