import pygame
from pygame.locals import *

from config import *
from player import Player
from maze import Maze

#Ouverture et configuration de la fenêtre Pygame 
pygame.init()
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
icon = pygame.image.load(icon_sprite)
pygame.display.set_icon(icon)
pygame.display.set_caption(title)
pygame.key.set_repeat(90, 50)

# Chargement des images
image_bg = pygame.image.load(background).convert()
image_bg = pygame.transform.scale(image_bg, (screen_size_x, screen_size_y))
image_lobby = pygame.image.load(lobby).convert_alpha()
image_lobby = pygame.transform.scale(image_lobby, (screen_size_x, screen_size_y))
image_victory = pygame.image.load(victory).convert_alpha()
image_victory = pygame.transform.scale(image_victory, (screen_size_x, screen_size_y))

# Definition des polices
font_title = pygame.font.SysFont("sylfaen", 100)
font_foot = pygame.font.SysFont("calibri", 30)

# Boucle infinie
while True:
    in_lobby, in_game = 1, 1
    in_victory = 1

    # Ecran d'accueil
    while in_lobby:
        pygame.time.Clock().tick(30)

        # Mise en forme du lobby
        text_title = font_title.render("DK IN THE MAZE!", True, (41,138,41))
        text_foot = font_foot.render("PRESS ANY KEY TO START", True, (0,0,0))
        screen.blit(image_lobby, (0,0))
        screen.blit(text_title, ((screen_size_x - text_title.get_rect().width) / 2, screen_size_x / 60))
        screen.blit(text_foot, ((screen_size_x - text_foot.get_rect().width) / 2,  0.96 * screen_size_y ))
        pygame.display.flip()
        
        # Gestion des évenements
        for event in pygame.event.get():            
            # Fermeture de l'app
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                quit()                
            # Lancement de la partie   
            elif event.type == KEYDOWN and event.key not in [K_ESCAPE, K_RIGHT]:
                    in_lobby = 0

  
    # Génération du labyrinthe et du personnage
    maze = Maze(cell_count_x, cell_count_y)
    maze.create()
    dk = Player(maze, dk_up, dk_down, dk_left, dk_right)    


    # En jeu
    while in_game:
        pygame.time.Clock().tick(30)

        # Gestion des évenements
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
        screen.blit(image_bg, (0,0))
        maze.show(screen)
        screen.blit(dk.direction, (dk.coord_x, dk.coord_y))
        pygame.display.flip()

        # Retour à l'écran d'accueil en cas de victoire
        if maze.structure[dk.cell_y, dk.cell_x] == 'E':
            in_game = 0
            in_victory = 1


    # Ecran de victoire
    while in_victory:
        pygame.time.Clock().tick(30)

        # Mise en forme de l'ecran de victoire
        text_victory = font_title.render("CONGRATULATIONS!", True, (175,34,26))
        text_instruction = font_foot.render("PRESS ANY KEY TO PLAY AGAIN", True, (0,0,0))
        screen.blit(image_victory, (0,0))
        screen.blit(text_victory, ((screen_size_x - text_victory.get_rect().width) / 2, screen_size_y / 15))        
        screen.blit(text_instruction, ((screen_size_x - text_foot.get_rect().width) / 2,  0.96 * screen_size_y ))
        pygame.display.flip()

        # Gestion des évenements        
        for event in pygame.event.get():            
            # Fermeture de l'app
            if event.type == QUIT:
                pygame.quit()
                quit()
            # Retour lobby  
            elif event.type == KEYDOWN:
                in_victory = 0
