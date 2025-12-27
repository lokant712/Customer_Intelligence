import csv
import os
from opensearchpy import OpenSearch
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = OpenSearch(
    hosts=[{"host": os.getenv("OPENSEARCH_HOST", "localhost"), "port": 9200}],
    http_compress=True
)

with open("data/customer_data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        vector = model.encode(row["text"]).tolist()

        doc = {
            "customer_id": row["customer_id"],
            "text": row["text"],
            "sentiment": row["sentiment"],
            "timestamp": row["timestamp"],
            "embedding": vector
        }

        client.index(index="customer_intelligence", body=doc)

print("CSV data indexed successfully")
