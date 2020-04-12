import pygame
from pygame.locals import *
import numpy as np

from constantes import *

level_structure = []
with open("levels/level_2.txt", "r") as files:
    for row in files:
        row_structure = []
        for char in row:
            if char != "\n":
                row_structure.append(char)
        level_structure.append(b)
level_structure = np.array(level_structure)

