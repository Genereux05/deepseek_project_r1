import os
import re
import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

class DeepSeekR1Engine:
    def __init__(self, folder_path="clean_documents", chunk_size=3):
        self.folder_path = folder_path
        self.chunk_size = chunk_size
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.chunks = []
        self.sources = []
        self.index = None
        self._prepare()

    def _nettoyer_texte(self, texte):
        texte = texte.replace('\ufeff', '')
        texte = re.sub(r'[^\w\s.,;:!?\'"()\[\]-]', '', texte)
        texte = re.sub(r'\s+', ' ', texte)
        return texte.strip()

    def _split_en_chunks(self, texte):
        phrases = re.split(r'(?<=[.!?]) +', texte)
        return [' '.join(phrases[i:i+self.chunk_size]) for i in range(0, len(phrases), self.chunk_size)]

    def _prepare(self):
        print("Chargement et découpage des documents...")
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                path = os.path.join(self.folder_path, filename)
                with open(path, "r", encoding="utf-8") as f:
                    contenu = f.read()
                contenu = self._nettoyer_texte(contenu)
                
                blocs = self._split_en_chunks(contenu)
                self.chunks.extend(blocs)
                self.sources.extend([filename] * len(blocs))

        print("Génération des vecteurs...")
        embeddings = self.model.encode(self.chunks)
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings))
        print("Indexation terminée.")

    def query(self, question, top_k=1):
        q_vec = self.model.encode([question])
        distances, indices = self.index.search(np.array(q_vec), top_k)
        results = []
        for i in indices[0]:
            results.append({
                "text": self.chunks[i],
                "source": self.sources[i]
            })
        return results[0] if results else {"text": "Aucune réponse trouvée.", "source": "N/A"}
