# import os
# import glob
# import importlib

# dossier_courant = os.path.dirname(__file__)

# for fichier in glob.glob(os.path.join(dossier_courant, "*.py")):
#     if not os.path.basename(fichier).startswith("__init__.py"):
#         module_name = os.path.basename(fichier).rsplit('.', 1)[0]
#         module = importlib.import_module(module_name)
#         print('*')
#         for nom_attribut in dir(module):
#             objet = getattr(module, nom_attribut)
#             if not nom_attribut.startswith("_"):  
#                 globals()[nom_attribut] = objet