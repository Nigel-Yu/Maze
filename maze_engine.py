import cell
import random

class Maze:
  def __init__(self, num_rows, num_cols):
    self.num_rows = num_rows
    self.num_cols = num_cols 
    self.grid = [[cell.Cell(r, c) for c in range(num_cols)] for r in range(num_rows)]

  def _inBounds(self, r, c):
    return (0 <= r < self.num_rows) and (0 <= c < self.num_cols) 
 
  # Randomized Depth-First Search Maze Generation / Recursive Backtracker
  def _carve(self, start):
    start.unvisited = False
    stack = [start] # Last In, First Out

    while stack:
      cur = stack[-1]
      unvisited_neighbors = []
      for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # checks 4 four neighbors
        pr = cur.r + dr # r prime
        pc = cur.c + dc # c prime
        if self._inBounds(pr, pc) and self.grid[pr][pc].unvisited:
          unvisited_neighbors.append((pr, pc))
      if unvisited_neighbors:
        nr, nc = random.choice(unvisited_neighbors) # "new" row/col
        next_cell = self.grid[nr][nc]
        
        # knock down walls
        if nr > cur.r: # new cell below
          cur.bottom = next_cell.top = False
        elif nr < cur.r: # new cell on top
          cur.top = next_cell.bottom = False
        elif nc > cur.c: # new cell on right
          cur.right = next_cell.left = False
        elif nc < cur.c: # new cell on left
          cur.left = next_cell.right = False

        next_cell.unvisited = False
        stack.append(next_cell)
      else:
        stack.pop()
      
      yield cur # returns current cell, saves progress
      
  def reset_maze(self):
    self.grid = [[cell.Cell(r, c) for c in range(self.num_cols)] for r in range(self.num_rows)]

  def generate_maze(self):
    return self._carve(self.grid[0][0])