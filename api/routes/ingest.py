from fastapi import APIRouter, UploadFile
from parsers.parser_choice import get_parser
from parsers.pdf import PDFparser
import magic


router = APIRouter()
# ingest 
@router.post("/ingest/")
async def upload_doc(file: UploadFile):
    #parse
    contents = await file.read()
    mime_type = magic.from_buffer(contents, mime=True)
    parser = get_parser(mime_type)#gets parser
    text_list = parser.parse(contents)
    
    #chunk


    #embeddings


    #store chunks and embeddings

    print(f"Received file: {file.filename}")
    print(f"Content type: {file.content_type}")
    print(f"File size: {len(contents)} bytes")
    print(f"mime type: { mime_type }")
    return {"filename": file.filename}
