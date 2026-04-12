
from parsers.pdf import PDFparser
PARSERS = {
    "application/pdf" : PDFparser(),

}

def get_parser(mime_type: str):
    parser = PARSERS.get(mime_type)
    if not parser:
        raise ValueError(f"Unsupported file type {mime_type}")
    return parser