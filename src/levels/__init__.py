from os import listdir as os_listdir
from os.path import dirname as os_path_dirname
from importlib import import_module

# Parcourir tous les fichiers Python dans le dossier actuel
current_dir = os_path_dirname(__file__)
for filename in os_listdir(current_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]  # Nom du module sans l'extension .py
        # Importer le fichier comme un sous-module
        import_module(f".{module_name}", package=__name__)