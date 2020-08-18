import pygame 
import math
from queue import PriorityQueue

width = 800
window = pygame.display.set_mode((width,width))
pygame.display.set_caption("A* ALGORITHM")


Grid_Colors = {"Red": (255,0,0), "Green":(0,255,0), "Blue":(0,0,255), "Yellow": (255,255,0), "White": (255,255,255), "Black": (0,0,0), "Purple": (255,0,255), "Orange": (255,165,0), "Grey": (128,128,128), "Cyan": (0, 255,255)}

class Block():
    
    def __init__(self, row, col, width, row_total):
        self.row = row
        self.col = col
        self.status = "blank"
        self.color = Grid_Colors["White"]
        self.x = row * width
        self.y = col * width
        self.width = width
        self.coords = [self.x, self.y]
        self.row_total = row_total
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0
        self.neighbors = []
        def set_status(self, status):
            self.status = status
            
    def get_pos(self):
        return self.row, self.col
        
    def is_closed(self):
        return self.color == Grid_Colors["Red"]
    
    def is_open(self):
        return self.color == Grid_Colors["Green"]

    def is_barrier(self):
        return self.color == Grid_Colors["Black"]

    def is_start(self):
        return self.color == Grid_Colors["Orange"]
    
    def is_end(self):
        return self.color == Grid_Colors["Purple"]

    def reset(self):
        self.color = Grid_Colors["White"]

    def make_closed(self):
        self.color = Grid_Colors["Red"]

    def make_open(self):
        self.color = Grid_Colors["Green"]

    def make_barrier(self):
        self.color = Grid_Colors["Black"]

    def make_start(self):
        self.color = Grid_Colors["Orange"]
    
    def make_end(self):
        self.color = Grid_Colors["Purple"]

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        if self.row < self.row_total -1 and not grid[self.row +1][self.col].is_barrier(): #Block below
            self.neighbors.append(grid[self.row+1][self.col])
        
        if self.row < self.row_total -1 and not grid[self.row -1][self.col].is_barrier(): #Block above
            self.neighbors.append(grid[self.row-1][self.col])
        
        if self.row < self.row_total -1 and not grid[self.row][self.col-1].is_barrier(): #Block left
            self.neighbors.append(grid[self.row][self.col-1])
        
        if self.row < self.row_total -1 and not grid[self.row][self.col+1].is_barrier(): #Block right
            self.neighbors.append(grid[self.row][self.col-1])
    
    def __lt__(self, other): #comparing blocks
        return False

def h(start_point, end_point):
    """ Heuristic for the distance between two points """
    x1 = start_point[0]
    x2 = end_point[0]
    y1 = start_point[1]
    y2 = end_point[1]
    return int(10*math.sqrt((x2-x1)**2+(y2-y1)**2))


def make_grid(rows, width):
    grid = []
    gap = width // rows #width of each cube

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            block = Block(i, j, gap, rows)
            grid[i].append(block)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, Grid_Colors["Grey"], (i, i*gap),(width, i*gap)) #horizontal grid lines
        for j in range(rows):
            pygame.draw.line(win, Grid_Colors["Grey"], (j*gap, 0), (j*gap, width))

def draw(win, grid, rows, width):
    win.fill(Grid_Colors["White"])

    for row in grid:
        for block in row:
            block.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    """Converts mouse click to grid position"""
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def main(win, width):
    num_rows = 50
    grid = make_grid(num_rows, width)

    start = None #start block
    end = None #end block

    started = False #keeps track of if algo has started
    run = True

    while run:
        draw(win, grid, num_rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                #stops user from input while algo is running
                continue

            if pygame.mouse.get_pressed()[0]: #Left mouse click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, num_rows, width)
                block = grid[row][col]
                if not start and block != end:
                    start = block
                    start.make_start()
                
                elif not end and block != start:
                    end = block
                    end.make_end()
                    
                elif block != start and block != end:
                    block.make_barrier()

            elif pygame.mouse.get_pressed()[2]: #Right mouse click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, num_rows, width)
                block = grid[row][col]
                block.reset()
                if block == start:
                    start = None
                elif block == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    pass
    pygame.quit()

main(window, width)