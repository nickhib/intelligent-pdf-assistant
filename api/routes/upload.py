from fastapi import APIRouter, UploadFile
from parsers.parser_choice import get_parser
from parsers.pdf import PDFparser
import magic


router = APIRouter()
# ingest 
@router.post("/ingest/")
async def upload_doc(file: UploadFile):

    print(f"Received file: {file.filename}")
    print(f"Content type: {file.content_type}")
    contents = await file.read()
    mime_type = magic.from_buffer(contents, mime=True)
    parser = get_parser(mime_type)
    text = parser.parse(contents)
    print(f"File size: {len(contents)} bytes")
    print(f"mime type: { mime_type }")
    return {"filename": file.filename}
