import pymupdf
## 
class PDFparser:
    def parse(self, contents: bytes) ->list[str]:
        doc = pymupdf.Document(stream=contents, filetype="pdf")
        blocks = []
        for page in doc:
            page_blocks = page.get_text("dict")["blocks"]
            for block in page_blocks:
                if block["type"] == 0:
                    block_text ="".join(
                        span["text"]
                        for line in block["lines"]
                        for span in line["spans"]
                    ).strip()
                    ## we strip to get rid of any trailing  " "
                    if block_text:
                        blocks.append(block_text)
        return blocks







        