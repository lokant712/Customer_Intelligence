import csv
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# 1. Load Model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
embeddings = []

# 2. Read Data
print("Reading data...")
with open("data/customer_data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        documents.append(row)
        embeddings.append(model.encode(row["text"]))

# 3. Create FAISS Index
print("Creating FAISS index...")
embeddings_array = np.array(embeddings).astype("float32")
dimension = embeddings_array.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings_array)

# 4. Save Index and Metadata
print("Saving index and metadata...")
faiss.write_index(index, "faiss_index.bin")

with open("metadata.json", "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=2)

print(f"Indexed {len(documents)} documents successfully.")
