
#  DeepSeek-R1 — Assistant de Recherche Sémantique

## Description du projet

DeepSeek Project est une application qui implémente une API permettant de poser des questions en texte ou en audio. L'application utilise le moteur **DeepSeek-R1** pour rechercher des réponses dans un corpus local de fichiers `.txt`. Les réponses sont renvoyées à la fois sous forme de texte et d'audio. 
Elle s’appuie sur un moteur vectoriel basé sur le modèle **DeepSeek-R1**, un système de reconnaissance vocale (**Vosk**) et une synthèse vocale (**gTTS**) pour restituer la réponse sous forme audio.


---

## Fonctionnalités principales

-  **Nettoyage de documents bruts** (.txt)
-  **Indexation vectorielle** des textes découpés en blocs (chunks)
-  **Requêtes utilisateur en texte ou audio (wav/mp3)**
-  **Recherche de la réponse la plus pertinente dans le corpus**
-  **Synthèse vocale** de la réponse
-  **Interface Web interactive (désactivable)**

---

## Architecture du projet

```
deepseek_project_r1/
│
├── app/
│   ├── main.py                   # Application FastAPI
│   ├── audio_utils.py            # Conversion texte -> audio et audio ->texte
│   ├── deepseek_interface.py     # Moteur de recherche vectorielle
│
├── audios/                       # Audios générés à la volée
├── clean_documents/             # Fichiers .txt déjà nettoyés et indexés
├── dirty_documents/             # Fichiers bruts non traités
├── vosk-model-small-fr-pguyot-0.3 # Modèle Vosk FR pour reconnaissance vocale
├── index.html                   # Interface Web (optionnelle)
├── nettoyage.py                 # Script de nettoyage initial
├── index_config.json            # Configuration de l'indexation
├── requirements.txt             # Fichier de dépendances
└── README.md                    # Documentation du projet
```

---

##  Installation & Exécution

###  Prérequis

- Python ≥ 3.8
- `pip install -r requirements.txt`
- Modèle Vosk téléchargé `vosk-model-small-fr-pguyot-0.3`

### Étapes de lancement

1. **Nettoyer les documents bruts :**

   python3 nettoyage.py

2. **Lancer l'application FastAPI :**

   uvicorn app.main:app --reload

3. **Accéder à l’interface Web :**

   http://127.0.0.1:8000/interface


4. **Tester l’API (Swagger UI) :**

   http://127.0.0.1:8000/docs


---

##  Fonctionnement Interne
    Nettoyage des Documents
    Le script nettoyage.py utilise la fonction nettoyer_texte pour supprimer les caractères inutiles et standardiser le contenu des fichiers .txt.

    Indexation Sémantique
    Le moteur DeepSeekR1Engine découpe les documents en blocs, génère des vecteurs d'embedding, et les indexe avec FAISS pour permettre des recherches rapides.

    Synthèse Vocale
    Le module audio_utils.py génère des fichiers audio à partir des réponses textuelles.

--- 

## Tests & Qualité

- Possibilité de tester via Swagger (`/docs`)
- Fichier audio généré pour chaque réponse (`audios/response_audio.mp3`)
- Comportement testé avec des entrées longues et des documents multiples
- Pour exécuter les tests unitaires, utilisez :python3 test.py
---

##  Livrables fournis

-  Code source complet (`*.py`)
-  Fichiers `.txt` nettoyés dans `clean_documents/`
-  Interface utilisateur (`index.html`)
-  README détaillé
-  Script de nettoyage (`nettoyage.py`)
-  Script d’indexation intégré
-  Données de test
-  API REST testable (`/docs`, `/ask-text`)

---

## Contributions

> 

---

## Auteur

**Nom** : TCHIAKPE Généreux Sèdjro Ronald  
**Email** : tchiakpegenereux05@gmail.com  
**Spécialité** : Intelligence Artificielle - IFRI  
**Année** : 2ᵉ année d'informatique