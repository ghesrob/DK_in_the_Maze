import random 
import numpy as np
import pygame
from pygame.locals import *

from config import *


class Maze:

    def __init__(self, length_x, length_y):
        """ Initialise le labyrinthe."""
        self.length_x, self.length_y = length_x, length_y
        # Initialisation d'une structure de labyrinthe vierge
        self.start_x, self.start_y = 0, 0
        self.end_x, self.end_y = length_x - 1, 0
        self.structure = np.full(fill_value = 'W', shape = (length_y, length_x))


    def find_valid_ways(self, coord_y, coord_x):
        """Détermine les directions valides à partir d'une cellule donnée."""
        delta = np.array([
            ['up', (-1,0), (-2,0)],
            ['down', (1,0), (2,0)],
            ['left', (0,-1), (0,-2)],
            ['right', (0,1), (0,2)]
            ])   
        valid_ways = []
        # On explore chaque direction
        for direction, (d1y, d1x), (d2y, d2x) in delta:           
            mid_x, mid_y = coord_x + d1x, coord_y + d1y
            end_x, end_y = coord_x + d2x, coord_y + d2y
            # On récupère les directions valides
            if 0 < end_x < self.length_x and 0 < end_y < self.length_y:
                if self.structure[end_y, end_x] == 'W':
                    valid_ways.append(((mid_y, mid_x), (end_y, end_x)))  
        return(valid_ways)


    def create(self):
        """Génère le labyrinthe.""" 
        current_cell = (random.randrange(1, self.length_y, 2), random.randrange(1, self.length_x, 2))
        self.structure[current_cell] = 'P'
        cell_stack = [current_cell]
        while cell_stack:
            valid_ways = self.find_valid_ways(*current_cell)
            if not valid_ways:
                cell_stack.pop()
                if cell_stack:
                    current_cell = cell_stack[-1]
                continue
            # Choisit une destination, et s'y déplace
            mid_cell, end_cell = random.choice(valid_ways)
            self.structure[mid_cell] = 'P'
            self.structure[end_cell] = 'P'
            current_cell = end_cell
            cell_stack.append(current_cell)     

        # Sélection de la case de départ
        valid_start_y = [y for y in range(self.length_y) if self.structure[y, 1] != "W"]
        self.start_y = random.choice(valid_start_y)
        self.structure[self.start_y, self.start_x] = 'S'        
        # Sélection de la case d'arrivée
        valid_end_y = [y for y in range(self.length_y) if self.structure[y, -2] != "W"]
        self.end_y = random.choice(valid_end_y)
        self.structure[self.end_y, self.end_x] = 'E'


    def show(self, window):
        """Affiche le labyrinthe à l'écran."""
        # Chargement des images
        wall_image = pygame.image.load(wall).convert_alpha()
        start_image = pygame.image.load(start).convert_alpha()
        banana_image = pygame.image.load(banana).convert_alpha()

        # Affichage des images
        pixel_y = 0
        for row in self.structure:
            pixel_x = 0
            for cell in row:
                if cell == "W":
                    window.blit(wall_image, (pixel_x, pixel_y))
                elif cell == "S":
                    window.blit(start_image, (pixel_x, pixel_y))
                elif cell == "E":
                    window.blit(banana_image, (pixel_x, pixel_y))                    
                pixel_x += cell_size
            pixel_y += cell_size
      