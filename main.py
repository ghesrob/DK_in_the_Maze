import pygame
from pygame.locals import *
from constantes import *
from player import Player
from level import Level
pygame.init()


#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((window_size, window_size))
#Icone
icone = pygame.image.load(icone_sprite)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(title)



# Boucle 
in_app = 1
while in_app:
    in_lobby = 1
    in_game = 1

    # Ecran d'accueil
    while in_lobby:
        pygame.time.Clock().tick(30)

        # Mise en forme du lobby
        image_lobby = pygame.image.load(lobby).convert_alpha()
        fenetre.blit(image_lobby, (0,0))
        pygame.display.flip()

        level_selected = 0
        
        for event in pygame.event.get():
            # Fermeture de l'app
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                in_app, in_lobby, in_game = 0, 0, 0

            # Choix du niveau    
            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    in_lobby = 0
                    level_selected = "L1"
                elif event.key == K_F2:
                    in_lobby = 0
                    level_selected = "L2"


    # Sortie de lobby - preparation du jeu 
    if level_selected != 0:
        background_image = pygame.image.load(background).convert()
        fenetre.blit(background_image, (0,0))
        pygame.display.flip()


    # En jeu
    while in_game:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # Fermeture de l'app 
            if event.type == QUIT:
                in_app, in_game = 0, 0

            # Retour lobby avec la touche échap    
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                in_game = 0
