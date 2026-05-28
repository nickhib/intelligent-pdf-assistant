

from transformers import AutoTokenizer, AutoModel


tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
def fixed_size(txt: str, size: int = 200, overlap: int =35) -> list[str]:
    all_Tokens = tokenizer.encode(txt)
    chunks = []
    for i in range(0,len(all_Tokens),(size-overlap)):
        chunks.append(tokenizer.decode(all_Tokens[i:i+size]))       
    return chunks

    # will take the text in get the maxed size of chunk and overlap size
    # then we will have our tokenizer which is made from the model we are going
    #