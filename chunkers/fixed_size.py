

def fixed_size(txt: str, size: int = 512, overlap: int =50) -> list[str]:
    chunks = []
    for i in range(0,len(txt),size-overlap):
        chunks.append(txt[i:i+size])        
    return chunks

