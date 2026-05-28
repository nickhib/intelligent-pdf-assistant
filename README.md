# intelligent-pdf-assistant
A RAG API that lets you upload PDFs and ask questions about them using semantic search
  + Claude.
# Architecture
    - Ingest: PDF - parse with library PyMuPDF - token-aware chunking (using all-MiniLM-L6-v2 tokenizer) - sentence-transformer

    embeddings are stored in ChromaDB
    - Query: store embed query with chromadb do a vector search grab top 5 chunks - create Claude prompt with context - return answer
# API endpoints
    - POST /ingest/ — upload a file, get back chunk count, store the embeddings
    - POST /query/ — send a question string, get back an LLM-generated response

# Setup / Quickstart
    set up your python enviorment: source venv/bin/activate
    to deactivate: deactivate
    pip install -r requirements.txt
    copy .env.example to .env
    set ANTHROPIC_API_KEY
    for development tests run fastapi dev
# Tech stack
    Tech stack — FastAPI, ChromaDB, sentence-transformers, PyMuPDF, Anthropic SDK