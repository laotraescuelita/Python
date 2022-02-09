import pygame
from pygame.locals import *
import sys
import numpy as np

#Iniciar la pantalla de pygame
pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode( (width, height), 0, 32)
pygame.display.set_caption("Hello, World!")
clock = pygame.time.Clock()

class Bars:
    def __init__(self, screen, width, widthbars, height):
        self.screen = screen
        self.widthgrid = width//widthbars
        self.status = np.zeros(self.widthgrid, dtype=int)
        self.bars = np.random.randint( 10, 400 , size= self.widthgrid )

    def draw(self):
        for i in  range( self.widthgrid ):
            if self.status[i] == 0:
                color = (255,255,255)
            elif self.status[i] == 1:
                color = (255,255,255)
            pygame.draw.rect(self.screen, color, Rect( (i*widthbars, height-self.bars[i] ), ( widthbars, self.bars[i] ) ) )


counter = 0
widthbars = 1
bars = Bars(screen, width, widthbars, height)

#Aqui se repite el canvas hasta que demos quit o cerremos la pantalla
while True:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    bars.draw()

    if counter <  bars.widthgrid :
        smallest_idx = counter
        for i in range( counter+1, bars.widthgrid ) :
            if bars.bars[smallest_idx] > bars.bars[i]:
                bars.status[i] = 1
                smallest_idx = i

        bars.bars[counter], bars.bars[smallest_idx] = bars.bars[smallest_idx], bars.bars[counter]

    else:
        print("Done")
    counter += 1

    pygame.display.update()


