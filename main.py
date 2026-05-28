from fastapi import FastAPI
from api.routes.ingest import router as ingest_router
from api.routes.query import router as query_router
from contextlib import asynccontextmanager
from embeddings.sentance_transformer import EmbeddingModel
import chromadb
import anthropic
from dotenv import load_dotenv
load_dotenv()
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.llm = anthropic.Anthropic()
    app.state.model = EmbeddingModel()
    app.state.chromadb_client = chromadb.PersistentClient(path="./chroma_db")
    app.state.collection =app.state.chromadb_client.get_or_create_collection(name="embeddings")
    yield
    


app = FastAPI(lifespan = lifespan)
### https://jalammar.github.io/illustrated-word2vec/ for more info on embeddings

app.include_router(ingest_router)
app.include_router(query_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}