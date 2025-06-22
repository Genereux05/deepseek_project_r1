import os
import re

def nettoyer_texte(texte):
    # Supprimer les caractères de contrôle (non imprimables) mais garder les accents
    texte = texte.replace('\ufeff', '')  # Enlève éventuellement le BOM
    texte = re.sub(r'[^\w\s.,;:!?\'"()\[\]-]', '', texte, flags=re.UNICODE)  # Supprime symboles bizarres
    texte = re.sub(r'\s+', ' ', texte)  # Réduit les espaces multiples
    return texte.strip()

# Dossiers
dossier_source = "dirty_documents"
dossier_sortie = "clean_documents"
os.makedirs(dossier_sortie, exist_ok=True)

# Nettoyage de tous les fichiers .txt
for nom_fichier in os.listdir(dossier_source):
    if nom_fichier.endswith(".txt"):
        chemin_source = os.path.join(dossier_source, nom_fichier)
        chemin_sortie = os.path.join(dossier_sortie, nom_fichier)
        with open(chemin_source, "r", encoding="utf-8") as f:
            texte = f.read()
        texte_nettoye = nettoyer_texte(texte)
        with open(chemin_sortie, "w", encoding="utf-8") as f:
            f.write(texte_nettoye)
