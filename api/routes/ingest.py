from fastapi import APIRouter, UploadFile, Request
from parsers.parser_choice import get_parser
from parsers.pdf import PDFparser
from chunkers.fixed_size import fixed_size
from pydantic import BaseModel
import magic


router = APIRouter()
# ingest 
@router.post("/ingest/")
async def upload_doc(request: Request, file: UploadFile):
    #parse
    model = request.app.state.model
    collection = request.app.state.collection
    contents = await file.read()
    mime_type = magic.from_buffer(contents, mime=True)
    parser = get_parser(mime_type)#gets parser
    text = parser.parse(contents)
    chunks = fixed_size(text, 200,30)# chunk it based on a fixed size. 
    #chunk
    embeddings = model.st_get_embeddings(chunks)
    collection.add(documents= chunks,
    embeddings=embeddings.tolist(),
    ids=[str(i) for i in range(len(chunks))]
    )
    return {"filename": file.filename, "chunks": len(chunks)}


