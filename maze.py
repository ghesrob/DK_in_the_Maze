import numpy as np
import pygame
from pygame.locals import *
import random 

# Fichier local
from constantes import *

class Maze:

    def __init__(self, length_x, length_y, start_x = 1, start_y = 1):
        self.length_x, self.length_y = length_x, length_y
        self.start_x, self.start_y = start_x, start_y
        self.structure = np.full(fill_value = 'm', shape = (length_x, length_y))


    def find_valid_ways(self, coord_x, coord_y):
        """ Méthode qui détermine les directions valides à partir de la cellule actuelle """
        
        delta = np.array([
            ['up', (0,-1), (0,-2)],
            ['down', (0,1), (0,2)],
            ['left', (-1,0), (-2,0)],
            ['right', (1,0), (2,0)]
            ])     
        valid_ways = []
        for direction, (d1x, d1y), (d2x, d2y) in delta:           
            mid_x, mid_y = coord_x + d1x, coord_y + d1y
            end_x, end_y = coord_x + d2x, coord_y + d2y
            if 0 < end_x < self.length_x and 0 < end_y < self.length_y:
                if self.structure[end_x, end_y] == 'm':
                    valid_ways.append((direction, (mid_x, mid_y), (end_x, end_y)))  
        return(valid_ways)



    def create(self):
        """ Méthode qui génère le labyrinthe """
        
        current_cell = (self.start_x, self.start_y)
        self.structure[current_cell] = '0'

        cell_stack = [current_cell]

        while cell_stack:
            valid_ways = self.find_valid_ways(*current_cell)

            if not valid_ways:
                cell_stack.pop()
                if cell_stack:
                    current_cell = cell_stack[-1]
                continue

            # Choisit une destination, et s'y déplace
            direction, mid_cell, end_cell = random.choice(valid_ways)
            self.structure[mid_cell] = '0'
            self.structure[end_cell] = '0'
            current_cell = end_cell
            cell_stack.append(current_cell)

    def show(self, window):
        """ Méthode qui affiche le niveau à l'écran """

        # Chargement des images
        wall_image = pygame.image.load(wall).convert_alpha()
        start_image = pygame.image.load(start).convert_alpha()
        banana_image = pygame.image.load(banana).convert_alpha()

        # Affichage des images
        pixel_y = 0
        for row in self.structure:
            pixel_x = 0
            for cell in row:
                if cell == "m":
                    window.blit(wall_image, (pixel_x, pixel_y))
                elif cell == "d":
                    window.blit(start_image, (pixel_x, pixel_y))
                elif cell == "a":
                    window.blit(banana_image, (pixel_x, pixel_y))                    
                pixel_x += cell_size
            pixel_y += cell_size
      