import wave
import json
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment


import os

from gtts import gTTS

def text_to_speech(text, output_file="response_audio.mp3"):
    try:
        audio_dir = "audios"
        os.makedirs(audio_dir, exist_ok=True)
        output_path = os.path.join(audio_dir, output_file)

        tts = gTTS(text=text, lang='fr')
        tts.save(output_path)
        return output_path
    except Exception as e:
        print(f"Erreur lors de la synthèse vocale : {e}")
        return None


def speech_to_text(file_path):
    # Vérifiez si le fichier est un MP3 et convertissez-le en WAV
    if file_path.endswith(".mp3"):
        wav_path = file_path.replace(".mp3", ".wav")
        audio = AudioSegment.from_file(file_path, format="mp3")
        audio.export(wav_path, format="wav")
        file_path = wav_path

    # Chargez le modèle Vosk
    model = Model("./vosk-model-small-fr-pguyot-0.3") 

    # Ouvrez le fichier WAV
    try:
        wf = wave.open(file_path, "rb")
    except wave.Error as e:
        raise ValueError(f"Erreur lors de l'ouverture du fichier WAV : {e}")

    # Initialisez le reconnaisseur
    rec = KaldiRecognizer(model, wf.getframerate())

    # Traitez l'audio pour extraire le texte
    result = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            result += res.get("text", "") + " "
    return result.strip()
