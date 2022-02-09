import pygame
from pygame.locals import *
import sys
from random import *
import numpy as np

pygame.init()
width = 600
height = 400
screen = pygame.display.set_mode( (width, height) , 0, 32)
pygame.display.set_caption("Quick sort")
clock = pygame.time.Clock()

bars =  np.random.randint(10, 300, (width,2) )
for bar in bars:
    bar[1] = 0
width_bars = 1

def quickSort(bars, start, end):   
    
    if start < end:     
        mid = partition( bars, start, end) 
        bars[mid][1] = 1
        quickSort( bars, start, mid-1)        
        quickSort( bars, mid+1, end )
    return bars
            

def partition(bars, start, end):     
    idx = start
    pivot = bars[idx][0]
    bars[idx][1] = 1
    while start < end: 
        while start < len( bars ) and bars[start][0] <= pivot:             
            bars[end][1] = 1
            start += 1                     
            bars[end][1] = 0
        
        while bars[end][0] > pivot:            
            end -= 1        
        
        if start < end:            
            bars[start][0],bars[end][0] = bars[end][0],bars[start][0]                  
    
    bars[idx][0],bars[end][0] = bars[end][0],bars[idx][0]         
    
    return end

start = 0 
end = len( bars ) - 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()    

    screen.fill((0,0,0))    

    A = quickSort(  bars, start, end )    
    
    for x in range( len(A) ):
        if A[x][1] == 0:
            color = (0,0,250)            
        elif A[x][1] == 1:
            color = (250,0,0)            
        elif A[x][1] == 2:
            color = (250,250,250)
        
        pygame.draw.rect(screen, color, (x*width_bars, 0, width_bars, A[x][0])  )

    clock.tick()
    pygame.display.update()