import time, sys, random, pygame
from pygame.locals import*
from random import seed
from random import randint

pygame.init()

W = 401
w = 20
DISPLAY = pygame.display.set_mode( (W, W) )
# GOLD = (218, 165, 32)
GOLD = (255, 255, 255)
run = True
cells = [[[True, True, True, True, False] for i in range(20)] for j in range(20)] # top-right-bottom-left
cells[0][0][4] = True


def hasUnvisitedNeighbours(i, j, cells ):
    unvisited = []
    if i-1 >= 0 : #top cell
        if cells[i-1][j][4] == False :
            unvisited.append( [i-1, j] )
    if j+1 < 20 : #right cell
        if cells[i][j+1][4] == False :
            unvisited.append( [i, j+1] )
    if i+1 < 20 : #bottom cell
        if cells[i+1][j][4] == False :
            unvisited.append( [i+1, j] )
    if j-1 >= 0 : #left cell
        if cells[i][j-1][4] == False :
            unvisited.append( [i, j-1] )
    return unvisited


def removeWalls( currentCell, nextCell, cells ):
    I = currentCell[0]
    J = currentCell[1]
    i = nextCell[0]
    j = nextCell[1]
    if i+1 == I and j == J : # next cell is the top one 
        cells[I][J][0] = False
        cells[i][j][2] = False
    if j-1 == J and i == I : # right cell is the next one
        cells[I][J][1] = False
        cells[i][j][3] = False
    if i-1 == I and j == J : # bottom cell  is the next one
        cells[I][J][2] = False
        cells[i][j][0] = False
    if j+1 == J and i == I : # left cell is the next one
        cells[I][J][3] = False
        cells[i][j][1] = False


def mazeAlgo( cells, currentCell ):
    i = currentCell[0]
    j = currentCell[1]
    cells[i][j][4] = True
    while len( hasUnvisitedNeighbours(i, j, cells) ) is not 0 :
        currentCell = [i, j]
        unvisited = hasUnvisitedNeighbours( i, j, cells )
        randUnvisited = randint( 0, len(unvisited)-1 )
        nextCell = [unvisited[randUnvisited][0], unvisited[randUnvisited][1]]
        removeWalls( currentCell, nextCell, cells )
        showCells(cells)
        mazeAlgo( cells, nextCell )


def showCells(cells):
    DISPLAY.fill((0, 0, 0))
    for i in range(20):
        for j in range(20):
            if cells[i][j][4]:
                pygame.draw.rect( DISPLAY, (255, 0, 0, 1), (j*w+1, i*w+1, 20, 20) )
            if cells[i][j][0]:
                pygame.draw.line( DISPLAY, GOLD, (j*w, i*w), ((j+1)*w, i*w), 1 )
            if cells[i][j][1]:
                pygame.draw.line( DISPLAY, GOLD, ((j+1)*w, i*w), ((j+1)*w, (i+1)*w), 1 )
            if cells[i][j][2]:
                pygame.draw.line( DISPLAY, GOLD, (j*w, (i+1)*w), ((j+1)*w, (i+1)*w), 1 )
            if cells[i][j][3]:
                pygame.draw.line( DISPLAY, GOLD, (j*w, i*w), (j*w, (i+1)*w), 1 )
    pygame.display.update()
    time.sleep(.05)

    

while( run ):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    showCells( cells )
    mazeAlgo(cells, [0, 0])