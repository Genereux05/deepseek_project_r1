import wave
import json
from vosk import Model, KaldiRecognizer


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
    model = Model("./vosk-model-small-fr-pguyot-0.3") 
    wf = wave.open(file_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    result = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            result += res.get("text", "") + " "
    return result.strip()
