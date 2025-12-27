# Customer Intelligence RAG

This project is a Retrieval-Augmented Generation (RAG) system that answers questions about customer data using OpenSearch and Google Gemini.

## Prerequisites

*   Docker and Docker Compose
*   A Google Gemini API Key (edit `llm.py` or set it up to read from env if you prefer)

## How to Run

1.  **Start OpenSearch**:
    ```bash
    docker-compose up -d opensearch
    ```
    Wait a moment for OpenSearch to start.

2.  **Set API Key**:
    Create a `.env` file or export the variable:
    ```bash
    export GEMINI_API_KEY="your_api_key_here"
    ```

3.  **Setup Index**:
    ```bash
    docker-compose run app python index_setup.py
    ```

3.  **Ingest Data**:
    ```bash
    docker-compose run app python ingest.py
    ```

4.  **Run the App**:
    ```bash
    docker-compose run app
    ```
    (Or `docker-compose run app python main.py` explicitly).

## Files
*   `data/customer_data.csv`: Your source data.
*   `docker-compose.yml`: Defines the services.
*   `Dockerfile`: Builds the Python app.
