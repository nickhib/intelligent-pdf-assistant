import pymupdf
## 
class PDFparser:
    def parse(self, contents: bytes) -> str:
        doc = pymupdf.Document(stream=contents, filetype="pdf")
        pages = ""
        for page in doc:
            pages.append(page.get_text().strip())
        return "".join(pages)







        