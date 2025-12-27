import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load Resources (Global to avoid reloading on every request)
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("faiss_index.bin")

with open("metadata.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

def semantic_search(query, k=100):
    # 1. Encode Query
    query_vector = model.encode(query).astype("float32").reshape(1, -1)
    
    # 2. Search FAISS Index
    distances, indices = index.search(query_vector, k)
    
    # 3. Retrieve Documents
    results = []
    for idx in indices[0]:
        if idx != -1:  # -1 means no match found
            results.append(documents[idx])
            
    return results
