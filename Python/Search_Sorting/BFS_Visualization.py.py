import pygame
from pygame.locals import *
import sys
import numpy as np

#Iniciar la pantalla de pygame
pygame.init()
width = 400
height = 400
screen = pygame.display.set_mode( (width, height), 0, 32)
pygame.display.set_caption("Hello, World!")
clock = pygame.time.Clock()

class Cells:
    def __init__( self, i, j ):
        self.i = i
        self.j = j
        self.wall = False
        self.visited = False
        self.prev = None
        self.neighbors = []

        if np.random.rand() < 0.4:
            self.wall = True

    def addNeighbors(self, grid):
        cols = grid.shape[0]
        rows = grid.shape[1]

        if self.j > 0:
            self.neighbors.append( grid[self.i][self.j-1] )
        if self.i < cols-1:
            self.neighbors.append( grid[self.i+1][self.j] )
        if self.j < rows-1:
            self.neighbors.append( grid[self.i][self.j+1] )
        if self.i > 0:
            self.neighbors.append( grid[self.i-1][self.j] )
        #diagonals
        if self.i < cols -1 and self.j < rows-1:
            self.neighbors.append( grid[self.i+1, self.j+1])
        if self.i < cols -1 and self.j > 0:
            self.neighbors.append( grid[self.i+1, self.j-1])
        if self.i > 0 and self.j < rows - 1:
            self.neighbors.append( grid[self.i-1, self.j+1])
        if self.i > 0 and self.j > 0:
            self.neighbors.append( grid[self.i-1, self.j-1])

class BFS:
    def __init__(self, screen, width, height, w):
        self.screen = screen
        self.w = w
        self.width = width
        self.height = height
        self.cols = self.width//self.w
        self.rows = self.height//self.w
        self.grid = np.empty( (self.rows, self.cols), dtype=object)
        self.x = 0
        self.y = 0

        for i in range( self.rows):
            for j in range( self.cols):
                self.grid[i][j] =  Cells( i, j )

        for i in range( self.rows):
            for j in range( self.cols):
                self.grid[i][j].addNeighbors(self.grid)

    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.x = self.grid[i][j].i * self.w
                self.y = self.grid[i][j].j * self.w
                pygame.draw.rect(self.screen, (255,255,255), Rect( (self.x,self.y), (self.w-1,self.w-1) ) )

                if self.grid[i][j].wall == True:
                    pygame.draw.rect(self.screen, (0,0,0), Rect( (self.x,self.y), (self.w-1,self.w-1) ) )

                if self.grid[i][j].visited == True:
                    pygame.draw.rect(self.screen, (50,255,50), Rect( (self.x,self.y), (self.w-1,self.w-1) ) )

                if self.grid[i][j] in path:
                    pygame.draw.rect(self.screen, (255,100,100), Rect( (self.x,self.y), (self.w-1,self.w-1) ) )

w = 20
queue = []
path = []

bfs = BFS( screen, width, height, w)
cols = bfs.cols
rows = bfs.rows

start = bfs.grid[0][0]
end = bfs.grid[rows-1][cols-1]
start.wall = False
end.wall = False

queue.append( start)
start.visited = True

#Aqui se repite el canvas hasta que demos quit o cerremos la pantalla
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #clock.tick(2)

    bfs.draw()

    if len( queue ) > 0:
        current = queue.pop()
        if current == end:
            temp = current
            while temp.prev:
                path.append( temp.prev )
                temp = temp.prev
            print( "Found!")
        else:
            for neighbor in current.neighbors:
                if not neighbor.visited and not neighbor.wall:
                    neighbor.visited = True
                    neighbor.prev = current
                    queue.append( neighbor )

    pygame.display.update()

