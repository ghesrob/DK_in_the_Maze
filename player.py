import pygame
from pygame.locals import * 

# Fichier local
from constantes import *


class Player:
    """ Classe permettant de créer un personnage """

    def __init__(self, level, sprite_up, sprite_down, sprite_left, sprite_right):
        # Position du perso
        self.cell_x = 0
        self.cell_y = 0
        self.coord_x = 0
        self.coord_y = 0

        # Sprites du perso
        self.sprite_up = pygame.image.load(sprite_up).convert_alpha()
        self.sprite_down = pygame.image.load(sprite_down).convert_alpha()
        self.sprite_left = pygame.image.load(sprite_left).convert_alpha()
        self.sprite_right = pygame.image.load(sprite_right).convert_alpha()

        # Direction du perso
        self.direction = self.sprite_right

        # Recuperation du niveau
        self.level = level


    def move(self, direction):
        """ Méthode permettant de déplacer le personnage """
        
        # Déplacement vers le haut
        if direction == "up":
            in_bounds = self.cell_y > 0
            if in_bounds:
                path_free = self.level.structure[self.cell_y - 1][self.cell_x] != 'm'
                if path_free:
                    self.cell_y -= 1
                    self.coord_y -= cell_size
            self.direction = self.sprite_up

        # Déplacement vers le bas
        elif direction == "down":
            in_bounds = self.cell_y < cell_count - 1            
            if in_bounds:
                path_free = self.level.structure[self.cell_y + 1][self.cell_x] != 'm'
                if path_free:
                    self.cell_y += 1
                    self.coord_y += cell_size
            self.direction = self.sprite_down

        # Déplacement vers la gauche
        elif direction == "left":
            in_bounds = self.cell_x > 0            
            if in_bounds:
                path_free = self.level.structure[self.cell_y][self.cell_x - 1] != 'm'
                if path_free:
                    self.cell_x -= 1
                    self.coord_x -= cell_size
            self.direction = self.sprite_left

        # Déplacement vers la droite
        elif direction == "right":
            in_bounds = self.cell_x < cell_count - 1            
            if in_bounds:
                path_free = self.level.structure[self.cell_y][self.cell_x + 1] != 'm'
                if path_free:
                    self.cell_x += 1
                    self.coord_x += cell_size
            self.direction = self.sprite_right
