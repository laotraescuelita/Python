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
j = 0
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
        key = bars.bars[ counter ]
        j = counter - 1
        while j >= 0 and key < bars.bars[j]:
            bars.bars[j+1] = bars.bars[j]
            bars.status[j+1], bars.status[j] = 1,1
            j -= 1
        bars.bars[j+1] = key
    else:
        print( "Done!")
    counter += 1

    pygame.display.update()


