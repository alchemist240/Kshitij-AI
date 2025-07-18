import json
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

# Load model once at top-level
model = SentenceTransformer('all-MiniLM-L6-v2')

def build_faiss_index(json_path, index_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = [item["input"] for item in data]
    embeddings = model.encode(questions)

    # Create FAISS index
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    # Save index
    faiss.write_index(index, index_path)

    # Save metadata (Q&A pairs) as pickle
    metadata_path = os.path.splitext(index_path)[0] + "_metadata.pkl"
    with open(metadata_path, "wb") as f:
        pickle.dump(data, f)

    print(f"Index built and saved to {index_path}")
    print(f"Metadata saved to {metadata_path}")

# ✅ Function for querying: used in retriever.py
def embed_query(query):
    return model.encode([query])[0]

def load_faiss_index(index_path, metadata_path):
    index = faiss.read_index(index_path)
    with open(metadata_path, "rb") as f:
        metadata = pickle.load(f)
    return index, metadata

if __name__ == "__main__":
    build_faiss_index("data/kshitij_profile.json", "data/vector_store/faiss_index")
