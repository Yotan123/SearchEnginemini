import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SearchEngine:
    def __init__(self, dataset_path="search_engine/dataset"):
        self.dataset_path = dataset_path
        self.documents = []
        self.filenames = []

        self._load_documents()
        self._vectorize()

    def _load_documents(self):
        for filename in os.listdir(self.dataset_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.dataset_path, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    self.documents.append(f.read())
                self.filenames.append(filename)

    def _vectorize(self):
        self.vectorizer = TfidfVectorizer()
        self.doc_vectors = self.vectorizer.fit_transform(self.documents)

    def search(self, query, top_n=5):
        query_vec = self.vectorizer.transform([query])
        similarity = cosine_similarity(query_vec, self.doc_vectors)[0]

        ranked_idx = np.argsort(similarity)[::-1]

        results = []
        for idx in ranked_idx[:top_n]:
            if similarity[idx] > 0:
                snippet = self.documents[idx][:200].replace("\n", " ") + "..."
                results.append({
                    "filename": self.filenames[idx],
                    "similarity": float(similarity[idx]),
                    "snippet": snippet
                })

        return results
