from fastapi import APIRouter, Request
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
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=5
    )
    chunks = results["documents"][0];
    ## will split chunks up by lines \n\n
    context = "\n\n".join(chunks)
    ## formatted string literal
    prompt = f"use the following context to answer the question. Context: {context}. Question: {body.query}"
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
        ) 
    answer = response.content[0].text;
    return {"answer": answer}
