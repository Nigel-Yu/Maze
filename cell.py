class Cell:
    def __init__(self, c, r):
        self.top = self.bottom = self.left = self.right = True # True = wall, False = open
        self.unvisited = True # all start as unvisited
        self.c = c
        self.r = r
        