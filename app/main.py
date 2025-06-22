from fastapi import FastAPI, UploadFile, File, Request
from pydantic import BaseModel
import shutil
import os

from app.audio_utils import text_to_speech, speech_to_text
from app.deepseek_interface import DeepSeekR1Engine
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

# Initialisation FastAPI
app = FastAPI()

# Moteur de recherche basé sur chunks (depuis clean_documents)
search_engine = DeepSeekR1Engine("clean_documents")

# Dossier audio
AUDIO_DIR = "audios"
os.makedirs(AUDIO_DIR, exist_ok=True)

# Rendre les fichiers audio accessibles publiquement
app.mount("/audios", StaticFiles(directory=AUDIO_DIR), name="audios")

# Interface HTML (si activée)
@app.get("/interface", response_class=HTMLResponse)
def interface():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# Route d'accueil simple
@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de recherche DeepSeek-R1 avec chunks."}

# Modèle pour les questions texte
class Question(BaseModel):
    question: str

@app.post("/ask-text/")
async def ask_text(q: Question, request: Request):
    result = search_engine.query(q.question)
    response_text = result["text"]
    source_file = result["source"]

    audio_path = text_to_speech(response_text)
    filename = os.path.basename(audio_path)
    url = request.url_for("audios", path=filename)

    return {
        "question": q.question,
        "response": response_text,
        "source_file": source_file,
        "audio_file": str(url)
    }

@app.post("/ask-audio/")
async def ask_audio(file: UploadFile = File(...), request: Request = None):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    question = speech_to_text(temp_path)
    result = search_engine.query(question)
    response_text = result["text"]
    source_file = result["source"]

    audio_path = text_to_speech(response_text)
    filename = os.path.basename(audio_path)
    os.remove(temp_path)

    url = request.url_for("audios", path=filename)

    return {
        "question_text": question,
        "response": response_text,
        "source_file": source_file,
        "audio_file": str(url)
    }
