import pygame
from pygame.locals import *

# Fichier local
from constantes import *


class Level:
    """ Classe permettant de créer un niveau """

    def __init__(self, level_selected):
        self.structure = []
        self.file = level_selected
        

    def create(self):
        """ Méthode qui génère la structure du niveau """
        with open(self.file, "r") as files:
            level_structure = []
            for row in files:
                row_structure = []
                for char in row:
                    if char != "\n":
                        row_structure.append(char)
                level_structure.append(row_structure)
        self.structure = level_structure


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