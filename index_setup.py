from opensearchpy import OpenSearch
import os

client = OpenSearch(
    hosts=[{"host": os.getenv("OPENSEARCH_HOST", "localhost"), "port": 9200}],
    http_compress=True
)

index_name = "customer_intelligence"

if client.indices.exists(index=index_name):
    client.indices.delete(index=index_name)

mapping = {
    "settings": {
        "index": {
            "knn": True
        }
    },
    "mappings": {
        "properties": {
            "customer_id": {"type": "keyword"},
            "text": {"type": "text"},
            "sentiment": {"type": "keyword"},
            "timestamp": {"type": "date"},
            "embedding": {
                "type": "knn_vector",
                "dimension": 384
            }
        }
    }
}

client.indices.create(index=index_name, body=mapping)
print("Index created:", index_name)
