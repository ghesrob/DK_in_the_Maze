import pygame
from pygame.locals import *

# Fichiers locaux
from constantes import *
from player import Player
from maze import Maze


#Ouverture et configuration de la fenêtre Pygame 
pygame.init()
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
icon = pygame.image.load(icon_sprite)
ingame_background = pygame.image.load(background).convert()
ingame_background = pygame.transform.scale(ingame_background, (screen_size_x, screen_size_y))
pygame.display.set_icon(icon)
pygame.display.set_caption(title)
pygame.key.set_repeat(90, 50)


# Boucle infinie
while True:
    in_lobby = 1
    in_game = 1

    # Ecran d'accueil
    while in_lobby:
        pygame.time.Clock().tick(30)

        # Mise en forme du lobby
        image_lobby = pygame.image.load(lobby).convert_alpha()
        image_lobby = pygame.transform.scale(image_lobby, (screen_size_x, screen_size_y))
        screen.blit(image_lobby, (0,0))
        pygame.display.flip()

        
        for event in pygame.event.get():
            
            # Fermeture de l'app
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                quit()

            # Lancement de la partie   
            elif event.type == KEYDOWN and event.key != K_ESCAPE:
                    in_lobby = 0


    # Sortie de lobby - preparation du jeu 
    # Génération du niveau et du personnage
    maze = Maze(cell_count_x, cell_count_y)
    maze.create()
    dk = Player(maze, dk_up, dk_down, dk_left, dk_right)
     

    # En jeu
    while in_game:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # Fermeture de l'app 
            if event.type == QUIT:
                pygame.quit()
                quit()

            # Retour lobby avec la touche échap    
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                in_game = 0

            # Gestion des déplacements
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    dk.move("up")
                elif event.key == K_DOWN:
                    dk.move("down")
                elif event.key == K_LEFT:
                    dk.move("left")
                elif event.key == K_RIGHT:
                    dk.move("right")

        # Rafraichissement de l'affichage
        screen.blit(ingame_background, (0,0))
        maze.show(screen)
        screen.blit(dk.direction, (dk.coord_x, dk.coord_y))
        pygame.display.flip()

        # Retour à l'écran d'accueil en cas de victoire
        if maze.structure[dk.cell_y, dk.cell_x] == 'a':
            in_game = 0
