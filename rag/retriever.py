import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

class RAGRetriever:
    def __init__(self, index_path, metadata_path):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.read_index(index_path)

        # Load the Q&A metadata stored in .pkl format
        with open(metadata_path, "rb") as f:
            self.qa_data = pickle.load(f)

    def retrieve(self, query, top_k=5):
        query_vec = self.model.encode([query])
        D, I = self.index.search(np.array(query_vec).astype("float32"), top_k)

        results = []
        for i in I[0]:
            if i < len(self.qa_data):
                results.append(self.qa_data[i])
        return results
