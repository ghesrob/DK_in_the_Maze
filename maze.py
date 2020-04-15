import pygame
from pygame.locals import *
import random 

# Fichier local
from constantes import *
from cell import Cell

class Maze:
    
    def __init__(self, nx, ny, ix=0, iy=0):
        """Initialize the maze grid.
        The maze consists of nx x ny cells and will be constructed starting
        at the cell indexed at (ix, iy).
        """
        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy
        self.maze_map = [[Cell(x, y) for y in range(ny)] for x in range(nx)]
        self.structure = []

    def cell_at(self, x, y):
        """Return the Cell object at (x,y)."""
        return self.maze_map[x][y]


    def find_valid_neighbours(self, cell):
        """Return a list of unvisited neighbours to cell."""

        delta = [('W', (-1,0)),
                 ('E', (1,0)),
                 ('S', (0,1)),
                 ('N', (0,-1))]
        neighbours = []
        for direction, (dx,dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour = self.cell_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours


    def make_maze(self):
        # Total number of cells.
        n = self.nx * self.ny
        cell_stack = []
        current_cell = self.cell_at(self.ix, self.iy)
        # Total number of visited cells during maze construction.
        nv = 1

        while nv < n:
            neighbours = self.find_valid_neighbours(current_cell)

            if not neighbours:
                # We've reached a dead end: backtrack.
                current_cell = cell_stack.pop()
                continue

            # Choose a random neighbouring cell and move to it.
            direction, next_cell = random.choice(neighbours)
            current_cell.knock_down_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            nv += 1

    def large_maze(self):
        large = [["X" if x in [0, 2*self.nx] or y in [0, 2*self.ny] else "O" for y in range(2 * self.ny + 1)] for x in range(2 * self.nx + 1)]

        for y in range(self.ny):
            for x in range(self.nx):
                if self.cell_at(x, y).walls["S"]:
                    large[2*x+1][2*(y+1)] = "X"
                if self.cell_at(x, y).walls["E"]:
                    large[2*(x+1)][2*y+1] = "X"
                large[2*x][2*y] = "X"
        self.structure =  list(map(list, zip(*large)))


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
                if cell == "X":
                    window.blit(wall_image, (pixel_x, pixel_y))
                pixel_x += cell_size
            pixel_y += cell_size
      