from sentence_transformers import SentenceTransformer
import numpy as np
import torch
#device is hardcoded but the rest we can define during creation of object
class EmbeddingModel:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2", batch_size: int = 32):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer(model_name, device=self.device)
        self.batch_size = batch_size 

    def st_get_embeddings(self, text: list[str]) -> np.ndarray:
        return self.model.encode(text , normalize_embeddings=True,show_progress_bar=len(text))