# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:15:14 2024

@author: utilisateur
"""

import pygame
import sys

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Gestion des clics sur des éléments')

# Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Définir les boutons comme des Rect
button1 = pygame.Rect(100, 100, 200, 50)  # x, y, width, height
button2 = pygame.Rect(100, 200, 200, 50)

def draw_buttons():
    pygame.draw.rect(screen, BLUE, button1)
    pygame.draw.rect(screen, RED, button2)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Récupérer les coordonnées de la souris
            mouse_x, mouse_y = event.pos
            
            # Vérifier si le clic est sur un bouton
            if button1.collidepoint(mouse_x, mouse_y):
                print("Button 1 cliqué")
            elif button2.collidepoint(mouse_x, mouse_y):
                print("Button 2 cliqué")
    
    # Remplir l'écran de blanc
    screen.fill(WHITE)
    
    # Dessiner les boutons
    draw_buttons()
    
    # Rafraîchir l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
