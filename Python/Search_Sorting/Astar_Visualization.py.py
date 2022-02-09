import pygame
from pygame.locals import *
import sys
import numpy as np

#Iniciar la pantalla de pygame
pygame.init()
width = 400
height = 400
screen = pygame.display.set_mode( (width, height), 0, 32)
pygame.display.set_caption("A*star algoritmo!")
clock = pygame.time.Clock()

#Cada celda sera un objeto que contendra su información, vecinos, distancias, etc.
class Cells:
    def __init__( self, i, j ):
        self.i = i
        self.j = j
        self.f = 0
        self.g = 0
        self.h = 0
        self.wall = False
        self.visited = False
        self.prev = None
        self.neighbors = []

        if np.random.rand() < 0.2:
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


#La clase que recorre la matriz con celdas se basa en dismiuir la distancia conciendo la distancia la objetivo.
class Astar:
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

        #La matriz almacena cada objeto celda es de n x m 
        for i in range( self.rows):
            for j in range( self.cols):
                self.grid[i][j] =  Cells( i, j )

        #Ahora se agregan los vecinos a la matriz.
        for i in range( self.rows):
            for j in range( self.cols):
                self.grid[i][j].addNeighbors(self.grid)

    #Esta función dibuja la matriz y el recorrido coloreando el sendero seguido y si finaliza el sendero que lo llevo al destino
    def draw(self):

        for i in range(self.rows):
            for j in range(self.cols):
                self.x = self.grid[i][j].i * self.w
                self.y = self.grid[i][j].j * self.w
                pygame.draw.rect(self.screen, (255,255,255), Rect( (self.x,self.y), (self.w-1,self.w-1) ) )

                if self.grid[i][j].wall == True:
                    pygame.draw.rect(self.screen, (0,0,0), Rect( (self.x,self.y), (self.w-1,self.w-1) ) )

                if self.grid[i][j] in openset:
                    pygame.draw.rect(self.screen, (0,255,0), Rect( (self.x,self.y), (self.w-1,self.w-1) ) )

                if self.grid[i][j] in closeset:
                    pygame.draw.rect(self.screen, (0,0,255), Rect( (self.x,self.y), (self.w-1,self.w-1) ) )

                if self.grid[i][j] in path:
                    pygame.draw.rect(self.screen, (255,0,0), Rect( (self.x,self.y), (self.w-1,self.w-1) ) )

    def heuristic(self, current, end):
        return np.sqrt( (current.j - end.j)**2 + (current.i**2 - end.i**2 ) )
        #return abs(current.i-end.i) + abs(current.j-end.j)

w = 10
openset = []
closeset = []
path = []

astar = Astar( screen, width, height, w)
cols = astar.cols
rows = astar.rows
start = astar.grid[0][0]
end = astar.grid[rows-1][cols-1]

openset.append( start )
start.wall = False
end.wall = False

#Aqui se repite el canvas hasta que demos quit o cerremos la pantalla
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    astar.draw()

    if len( openset ) > 0:
        idx = 0
        for i in range( len( openset ) ):
            if openset[i].f < openset[idx].f:
                idx = i
        current = openset[idx]

        if current == end:
            temp = current
            while temp.prev:
                path.append( temp.prev )
                temp = temp.prev
            print( "Done!")

        openset.remove( current )
        closeset.append( current )

        for neighbor in current.neighbors:
            if neighbor in closeset or neighbor.wall:
                continue
            tempg = current.g + 1
            newpath = False

            if neighbor in openset:
                if tempg < neighbor.g:
                    neighbor.g = tempg
                    newpath = True
            else:
                neighbor.g = tempg
                newpath = True
                openset.append( neighbor )

            if newpath:
                neighbor.h = astar.heuristic( neighbor, end )
                neighbor.f = neighbor.g + neighbor.h
                neighbor.prev = current

    pygame.display.update()
