class Cell:
    """ Classe représentant une case du labyrinthe """

    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}


    def has_all_walls(self):
        """ Méthode qui vérifie qu'une case a tous ses murs """
        return all(self.walls.values())


    def knock_down_wall(self, other, wall):
        """ Retire le mur séparant une case d'une de ses voisines """
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False

