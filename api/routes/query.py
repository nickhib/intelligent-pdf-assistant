from fastapi import APIRouter, Request, HTTPException
from querytype import QueryReq

router = APIRouter()
# what chromadb will return on query
# class QueryResult(TypedDict):
#    ids: List[IDs]
#    embeddings: Optional[List[Embeddings]]
#    documents: Optional[List[List[Document]]]
#    uris: Optional[List[List[URI]]]
#    metadatas: Optional[List[List[Metadata]]]
#    distances: Optional[List[List[float]]]
#    included: Include
@router.post("/query/")
async def query_docs(request: Request, body: QueryReq):
    model = request.app.state.model
    collection = request.app.state.collection
    query_embedding = model.st_get_embeddings([body.query])
    client = request.app.state.llm;
    results = None
    prompt = ""
    try:
        results = collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=5
        )
        chunks = results["documents"][0];
        context = "\n\n".join(chunks)
        prompt = f"use the following context to answer the question. if the answer isnt there say so. Context: {context}. Question: {body.query}"
    except Exception:
        prompt = f"Question: {body.query}"
    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        ) 
    except Exception as exc:
         print(f"Failed: {str(exc)}")
         raise HTTPException(status_code=502, detail=str(exc))
    answer = response.content[0].text;
    return {"answer": answer}
