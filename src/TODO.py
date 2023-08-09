# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 18:04:20 2023

@author: zackary.vanche
"""

"""
Si vous affichez du texte avec Pygame dans une fenêtre de jeu et que vous souhaitez que le texte revienne à la ligne automatiquement lorsque la fenêtre est trop petite pour afficher tout le texte, vous devrez implémenter cette fonctionnalité vous-même en manipulant le texte avant de l'afficher.

Voici une approche générale que vous pouvez suivre :

Mesurer la largeur du texte : Utilisez la fonction pygame.font.Font pour créer une instance de la police que vous utilisez pour afficher le texte. Ensuite, utilisez la méthode font.size(text) pour mesurer la largeur du texte en pixels.

Calculer la largeur de la fenêtre : Obtenez la largeur actuelle de la fenêtre de jeu à l'aide de pygame.display.get_surface().get_width().

Vérifier la largeur du texte : Comparez la largeur du texte avec la largeur de la fenêtre. Si la largeur du texte dépasse la largeur de la fenêtre, vous pouvez diviser le texte en plusieurs lignes pour qu'il s'ajuste correctement.

Couper le texte en lignes : Divisez le texte en morceaux de manière à ce qu'ils puissent être affichés correctement sur plusieurs lignes. Vous pouvez utiliser l'algorithme de découpe de mots pour séparer le texte en mots individuels et le placer sur plusieurs lignes.

Afficher le texte ligne par ligne : Utilisez une boucle pour parcourir les morceaux de texte et utilisez la fonction blit() pour afficher chaque morceau de texte à la position appropriée sur l'écran. Assurez-vous de décaler la position en Y pour chaque ligne.

Gérer le débordement vertical : Si le texte coupé en plusieurs lignes dépasse également la hauteur de la fenêtre, vous devrez décider comment gérer le débordement vertical, par exemple en utilisant un système de défilement ou en limitant le nombre de lignes affichées.

Rafraîchir l'affichage : Après avoir affiché le texte correctement sur plusieurs lignes, assurez-vous de rafraîchir l'affichage en utilisant pygame.display.flip().

N'oubliez pas de tenir compte de la hauteur de la police (ascendantes et descendantes) lors du calcul des positions verticales pour chaque ligne de texte.

Il s'agit d'une solution générale, et les détails exacts dépendront de la structure de votre code et de la manière dont vous gérez l'affichage du texte dans votre jeu Pygame.
"""

import pygame
import sys

pygame.init()

# Configuration de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text Wrapping Example")

# Configuration de la police
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

# Texte à afficher
text = "Ceci est un exemple de texte long qui peut nécessiter un retour à la ligne automatique si la fenêtre est trop petite."

# Division du texte en lignes
words = text.split()
lines = []
current_line = words[0]
for word in words[1:]:
    test_line = current_line + " " + word
    if font.size(test_line)[0] <= width:
        current_line = test_line
    else:
        lines.append(current_line)
        current_line = word
lines.append(current_line)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    y = height // 2 - len(lines) * font.get_height() // 2
    for line in lines:
        rendered_text = font.render(line, True, text_color)
        screen.blit(rendered_text, (10, y))  # Alignement à gauche (10 pixels de marge)
        y += font.get_height()

    pygame.display.flip()

pygame.quit()
sys.exit()