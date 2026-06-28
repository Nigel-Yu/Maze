import pygame
import maze_engine

pygame.init()
rows = int(input("Number of Rows: "))
cols = int(input("Number of Cols: "))
cell_size = 100
screen = pygame.display.set_mode((cell_size * cols, cell_size * rows))
running = True
maze = maze_engine.Maze(rows, cols)
maze.generate_maze()

def draw(): 
   for row in maze.grid:
        for cell in row:
            r = cell.r
            c = cell.c
            if cell.left:
                draw_line((r, c), (r + 1, c))
            if cell.right:
                draw_line((r, c + 1), (r + 1, c + 1))
            if cell.top:
                draw_line((r, c), (r, c + 1))
            if cell.bottom:
                draw_line((r + 1, c), (r + 1, c + 1))
 
def draw_line(start, end):
    start_pixel = (start[1] * cell_size, start[0] * cell_size) # (row, col) -> (x, y)
    end_pixel = (end[1] * cell_size, end[0] * cell_size)
    pygame.draw.line(screen, "ghostwhite", start_pixel, end_pixel)

while running:
    for event in pygame.event.get(): # runs until window is closed
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print('Maze Resetting...')
                maze.reset_maze()
                maze.generate_maze()            

    screen.fill("black")
    draw()
    pygame.display.flip()
