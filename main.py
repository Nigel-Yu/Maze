import pygame
import maze_engine

pygame.init()
rows = int(input("Number of Rows: "))
cols = int(input("Number of Cols: "))
cell_size = 50
clock = pygame.time.Clock()
screen = pygame.display.set_mode((cell_size * cols, cell_size * rows))
running = True

def create_maze():
    global maze, maze_generator, current_cell
    maze = maze_engine.Maze(rows, cols)
    maze_generator = maze.generate_maze()
    current_cell = None

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

def highlight(cell, color):
    rect = pygame.Rect(cell.c * cell_size, cell.r * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, color, rect)

create_maze()
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # runs until window is closed
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print('Maze Resetting...')
                create_maze()

    if maze_generator is not None:
        try:
            current_cell = next(maze_generator)    
        except StopIteration:
            maze_generator = None
    
    screen.fill("black")
    if current_cell is not None:
        highlight(current_cell, "aqua")
    draw()
    pygame.display.flip()
    # print(f"Current cell: {current_cell.r, current_cell.c}")
    clock.tick(20)