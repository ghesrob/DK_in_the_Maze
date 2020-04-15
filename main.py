import pygame
from pygame.locals import *

# Fichiers locaux
from constantes import *
from player import Player
from maze import Maze
from cell import Cell


#Ouverture et configuration de la fenêtre Pygame 
pygame.init()
window = pygame.display.set_mode((window_size, window_size))
icon = pygame.image.load(icon_sprite)
pygame.display.set_icon(icon)
pygame.display.set_caption(title)
pygame.key.set_repeat(90, 100)

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
        window.blit(image_lobby, (0,0))
        pygame.display.flip()

        
        for event in pygame.event.get():
            # Fermeture de l'app
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                in_app, in_lobby, in_game = 0, 0, 0
                level_selected = 0

            # Choix du niveau    
            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    in_lobby = 0
                    level_selected = level_1
                elif event.key == K_F2:
                    in_lobby = 0
                    level_selected = level_2


    # Sortie de lobby - preparation du jeu 
    if level_selected:
        # Génération du niveau et du personnage
        #stage = Level(level_selected)
        #stage.create()
        maze = Maze(7, 7, 0, 0)
        maze.make_maze()
        maze.large_maze()
        dk = Player(maze, dk_up, dk_down, dk_left, dk_right)

        # Setup du jeu et affichage de l'écran
        background_image = pygame.image.load(background).convert()
        #window.blit(background_image, (0,0))
        #stage.show(window)        


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
        window.blit(background_image, (0,0))
        maze.show(window)
        window.blit(dk.direction, (dk.coord_x, dk.coord_y))
        pygame.display.flip()

        # Retour à l'écran d'accueil en cas de victoire
        if maze.structure[dk.cell_y][dk.cell_x] == 'a':
            in_game = 0