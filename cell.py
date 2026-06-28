class Cell:
    def __init__(self, r, c):
        self.top = self.bottom = self.left = self.right = True # True = wall, False = open
        self.unvisited = True # all start as unvisited
        self.r = r
        self.c = c