import os
import re

def replace_function_names(directory):
    """
    Remplace les noms des fonctions dans tous les fichiers .py du répertoire donné
    uniquement si le nom commence par 'level_'.
    - Les noms de fonctions contenant '_aux' deviennent 'aux'.
    - Les autres noms de fonctions deviennent 'f'.
    
    Args:
        directory (str): Chemin vers le dossier contenant les fichiers Python.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".py"):  # Vérifie que le fichier est un fichier Python
            filepath = os.path.join(directory, filename)

            # Lire le contenu du fichier
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

            # Remplacer les noms des fonctions correspondant au critère
            modified_content = re.sub(
                r"def\s+(level_[a-zA-Z0-9_]*)\s*\(",
                lambda match: f"def {'aux' if '_aux' in match.group(1) else 'f'}(",
                content
            )

            # Réécrire le fichier avec les modifications
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(modified_content)

            print(f"Modifications apportées au fichier : {filename}")

# Exemple d'utilisation
directory_path = "./levels"  # Remplacez par le chemin de votre dossier
replace_function_names(directory_path)
