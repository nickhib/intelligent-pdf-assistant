from fastapi import FastAPI
from api.routes.upload import router as upload_router

app = FastAPI()
### https://jalammar.github.io/illustrated-word2vec/ for more info on embeddings

app.include_router(upload_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}