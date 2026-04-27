from fastapi import FastAPI
from api.routes.ingest import router as ingest_router

app = FastAPI()
### https://jalammar.github.io/illustrated-word2vec/ for more info on embeddings

app.include_router(ingest_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}