from sentence_transformers import SentenceTransformer
from opensearchpy import OpenSearch
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

client = OpenSearch(
    hosts=[{"host": os.getenv("OPENSEARCH_HOST", "localhost"), "port": 9200}],
    http_compress=True
)

def semantic_search(query, k=5):
    query_vector = model.encode(query).tolist()

    body = {
        "size": k,
        "query": {
            "knn": {
                "embedding": {
                    "vector": query_vector,
                    "k": k
                }
            }
        }
    }

    response = client.search(
        index="customer_intelligence",
        body=body
    )

    hits = response["hits"]["hits"]
    return [hit["_source"]["text"] for hit in hits]
