import pygame
import math
from queue import PriorityQueue

WIDTH = 1000
HEIGHT = 600
COLS = 100
ROWS = 60
WIN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Node:
    def __init__(self, row, col, width, height, total_rows, total_columns):
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.x = col * width
        self.y = row * height
        self.total_rows = total_rows
        self.total_columns = total_columns
        self.color = WHITE
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def update_nieghbors(self, grid):
        self.neighbors = []

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # down
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # up
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # left
                    self.neighbors.append(grid[self.row][self.col - 1])

        if self.col < self.total_columns - 1 and not grid[self.row][self.col + 1].is_barrier(): # right
            self.neighbors.append(grid[self.row][self.col + 1])

    def __lt__(self, other):
        return False

    # def __repr__(self):
    #     return(f"node h{self.height} w{self.width}")

        
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
    global path_length
    path_length = 0
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()
        path_length += 1

def a_star_algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw() # comment this line to disable visualization. Makes it WAY faster when commented

        if current != start:
            current.make_closed()

    return False

def make_grid(rows, columns, width, height):
    grid = []
    vgap = height // rows # vertical gap
    hgap = width // columns # horizontal gap
    for i in range(rows):
        grid.append([])
        for j in range(columns):
            node = Node(i, j, hgap, vgap, rows, columns)
            grid[i].append(node)

    return grid

def draw_grid(win, rows, columns, width, height):
    vgap = height // rows # vertical gap
    hgap = width // columns # horizontal gap
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * vgap), (width, i * vgap))
    for j in range(columns):
        pygame.draw.line(win, GREY, (j * hgap, 0), (j * hgap, height))

def draw(win, grid, rows, columns, width, height):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, columns, width, height)
    pygame.display.update()

def get_clicked_pos(pos, rows, columns, width, height):
    vgap = height // rows # vertical gap
    hgap = width // columns # horizontal gap
    x, y = pos

    row = y // vgap
    col = x // hgap

    # print(row, col)
    return row, col

def main(win, width, height, ROWS, COLS):
    grid = make_grid(ROWS, COLS, width, height)

    start = None
    end = None
    run = True

    while run:
        draw(win, grid, ROWS, COLS, width, height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit
                run = False

            if pygame.mouse.get_pressed()[0]: # lmb
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, COLS, width, height)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: #rmb
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, COLS, width, height)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    print("Finding path...")
                    for row in grid:
                        for node in row:
                            node.update_nieghbors(grid)

                    result = a_star_algorithm(lambda: draw(win, grid, ROWS, COLS, width, height), grid, start, end)
                    if result == False:
                        print("Unable to find path")
                    else:
                        print(f"Found path of length {path_length}")

                if event.key == pygame.K_c:
                    print("Board cleared!")
                    start = None
                    end = None
                    grid = make_grid(ROWS, COLS, width, height)

                if event.key == pygame.K_r:
                    print("Reset path")
                    for row in grid:
                        for node in row:
                            if node.color == RED or node.color == GREEN or node.color == PURPLE:
                                node.reset()
                            node.draw(win)

    pygame.quit()


main(WIN, WIDTH, HEIGHT, ROWS, COLS)

