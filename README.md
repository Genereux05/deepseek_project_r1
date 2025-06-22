# DeepSeek Project avec DeepSeek-R1

## Description

DeepSeek Project est une application qui implémente une API permettant de poser des questions en texte ou en audio. L'application utilise le moteur **DeepSeek-R1** pour rechercher des réponses dans un corpus local de fichiers `.txt`. Les réponses sont renvoyées à la fois sous forme de texte et d'audio.

Le projet inclut des fonctionnalités de nettoyage de texte, d'indexation sémantique, et de génération de réponses audio.

---

## Fonctionnalités

- **Nettoyage des documents** : Les fichiers bruts sont nettoyés pour supprimer les caractères inutiles et standardiser le contenu.
- **Indexation sémantique** : Les documents sont découpés en blocs et indexés à l'aide de vecteurs d'embedding pour permettre des recherches rapides et précises.
- **Recherche de réponses** : Le moteur DeepSeek-R1 trouve les réponses les plus pertinentes dans le corpus.
- **Synthèse vocale** : Les réponses textuelles sont converties en audio pour une expérience utilisateur enrichie.
- **Support multilingue** : Le projet utilise le modèle Vosk pour la reconnaissance vocale en français.

---

## Structure du Projet
deepseek_project_r1
    app
        __pycache__
            # Fichiers compilés Python
        audio_utils.py
        deepseek_interface.py
        main.py
    audios
    clean_documents
        ## Contient les documents utiliés pour l'indexation deja nettoyés grace a nettoyage.py
    dirty_documents
        ## Documents au format bruts
    vosk-model-small-fr-pguyot-0.3/
        ##Model vosk pour la reconnaissance vocale
    nettoyage.py
        # Script de nettoyage des documents
    requirements.txt
        Dépendances Python
    index.html
        #Interface utilisateur web 
    index_config.json
        # Configuration de l'indexation
    README.md
        # Documentation du projet

---

## Prérequis

- **Python 3.8+**
- **Dépendances** : Installées via `requirements.txt`
- **Modèle Vosk** : Inclus dans le dossier `vosk-model-small-fr-pguyot-0.3`

---

## Installation

1. Clonez le dépôt :

   git clone https://github.com/Genereux05/deepseek_project_r1.git
   
   cd deepseek_project_r1

3. Installez les dépendances :
    pip install -r requirements.txt

4. Assurez-vous que le modèle Vosk est présent dans le dossier vosk-model-small-fr-pguyot-0.3.

## Utilisation

1. Nettoyage des documents
    Exécutez le script nettoyage.py pour nettoyer les fichiers bruts :

    python3 nettoyage.py

2. Lancer l'application
    Démarrez l'API en exécutant:
    
    uvicorn app.main:app --reload 

3. Interface utilisateur3

    120.0.0.1:8000/interface
    ""pour interagir avec l'application via une interface web.""

# Fonctionnement Interne
    Nettoyage des Documents
    Le script nettoyage.py utilise la fonction nettoyer_texte pour supprimer les caractères inutiles et standardiser le contenu des fichiers .txt.

    Indexation Sémantique
    Le moteur DeepSeekR1Engine découpe les documents en blocs, génère des vecteurs d'embedding, et les indexe avec FAISS pour permettre des recherches rapides.

    Synthèse Vocale
    Le module audio_utils.py génère des fichiers audio à partir des réponses textuelles.

    Tests
    Pour exécuter les tests unitaires, utilisez :

    python3 test.py

# Contributions


# Auteurs
    Nom de l'auteur : TCHIAKPE Généreux Sèdjro Ronald
    linkedIn:  Généreux TCHIAKPE
    Email: tchiakpegenereux05@gmail.com
