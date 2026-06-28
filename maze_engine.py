import cell
import random

class Maze:
  def __init__(self, num_rows, num_cols):
    self.num_rows = num_rows
    self.num_cols = num_cols 
    self.grid = [[cell.Cell(c, r) for c in range(num_cols)] for r in range(num_rows)]

  def inBounds(self, r, c):
    return (0 <= r < self.num_rows) and (0 <= c < self.num_cols) 
 
  # Randomized Depth-First Search Maze Generation / Recursive Backtracker
  def carve(self, cell):
    cell.unvisited = False
    while True:
      unvisited_neighbors = []
      for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # checks 4 four neighbors
        pr = cell.r + dr # r prime
        pc = cell.c + dc # c prime
        if self.inBounds(pr, pc) and self.grid[pr][pc].unvisited:
          unvisited_neighbors.append((pr, pc))
      if not unvisited_neighbors:
        break
      nr, nc = random.choice(unvisited_neighbors) # "new" row/col
      n_cell = self.grid[nr][nc]
      
      # knock down walls
      if nr < cell.r: # new cell below
        cell.bottom = n_cell.top = False
      elif nr > cell.r: # new cell on top
        cell.top = n_cell.bottom = False
      elif nc > cell.c: # new cell on right
        cell.right = n_cell.left = False
      elif nc < cell.c: # new cell on left
        cell.left = n_cell.right = False

      self.carve(n_cell)

  def generate_maze(self):
    self.carve(self.grid[0][0])