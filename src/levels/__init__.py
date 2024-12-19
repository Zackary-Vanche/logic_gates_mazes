import os
import importlib

# Parcourir tous les fichiers Python dans le dossier actuel
current_dir = os.path.dirname(__file__)
for filename in os.listdir(current_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]  # Nom du module sans l'extension .py
        # Importer le fichier comme un sous-module
        importlib.import_module(f".{module_name}", package=__name__)