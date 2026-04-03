# Customer Intelligence RAG (FAISS Edition)

This project answers questions about customer data using simple local vector search (FAISS) and Google Gemini.

## Prerequisites

*   Python 3.9+
*   Google Gemini API Key

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set API Key**:
    Windows (PowerShell):
    ```powershell
    $env:GEMINI_API_KEY="your_api_key_here"
    ```
    Mac/Linux:
    ```bash
    export GEMINI_API_KEY="your_api_key_here"
    ```

## How to Run

1.  **Ingest Data** (Run this once or whenever data changes):
    ```bash
    python ingest.py
    ```
    This creates `faiss_index.bin` and `metadata.json`.

2.  **Run the Web App**:
    ```bash
    streamlit run app.py
    ```
    Open the URL shown (usually `http://localhost:8501`).

3.  **Run the Telegram Bot**:
    *   **Prerequisite**: Create a bot with [@BotFather](https://t.me/BotFather) and get your token.
    *   **Set Token**:
        ```powershell
        $env:TELEGRAM_BOT_TOKEN="your_token"
        ```
    *   **Run**:
        ```bash
        python telegram_bot.py
        ```
    *   **Commands**:
        *   `/start`: Welcome message.
        *   `/ping`: Check connectivity.
        *   Any text: Queries the customer data.
