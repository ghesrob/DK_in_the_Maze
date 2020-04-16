import pygame
from pygame.locals import * 

# Fichier local
from constantes import *


class Player:
    """Classe permettant de créer et déplacer un personnage sur un labyrinthe."""

    def __init__(self, maze, sprite_up, sprite_down, sprite_left, sprite_right):
        """ Initialise un personnage.
        Un personnage est caractérisé par sa position à l'écran (en cases et en pixels), son orientation et les 
        quatres sprites associés à chacune des orientations possibles. Il est de plus associé au labyrinthe de la partie.
        """
        # Position du personnage
        self.cell_x, self.cell_y = maze.start_x, maze.start_y
        self.coord_x, self.coord_y = self.cell_x * cell_size, self.cell_y * cell_size
        # Sprites du personnage
        self.sprite_up = pygame.image.load(sprite_up).convert_alpha()
        self.sprite_down = pygame.image.load(sprite_down).convert_alpha()
        self.sprite_left = pygame.image.load(sprite_left).convert_alpha()
        self.sprite_right = pygame.image.load(sprite_right).convert_alpha()
        # Orientation du personnage
        self.direction = self.sprite_down
        # Recuperation du niveau
        self.maze = maze


    def move(self, direction):
        """Déplace le personnage selon une direction, si ce déplacement est possible."""       
        # Déplacement vers le haut
        if direction == "up" and self.cell_y > 0:
            if self.maze.structure[self.cell_y - 1, self.cell_x] != 'W':
                self.cell_y -= 1
                self.coord_y -= cell_size
            self.direction = self.sprite_up

        # Déplacement vers le bas
        elif direction == "down" and self.cell_y < cell_count_y - 1:
            if self.maze.structure[self.cell_y + 1, self.cell_x] != 'W':
                self.cell_y += 1
                self.coord_y += cell_size
            self.direction = self.sprite_down

        # Déplacement vers la gauche
        elif direction == "left" and self.cell_x > 0 :
            if self.maze.structure[self.cell_y, self.cell_x - 1] != 'W':
                self.cell_x -= 1
                self.coord_x -= cell_size
            self.direction = self.sprite_left

        # Déplacement vers la droite
        elif direction == "right" and self.cell_x < cell_count_x - 1:
            if self.maze.structure[self.cell_y, self.cell_x + 1] != 'W':
                self.cell_x += 1
                self.coord_x += cell_size
            self.direction = self.sprite_right
