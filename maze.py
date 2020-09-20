import time, pygame, sys

from pygame.locals import*
pygame.init()

W = 401
H = 401
DISPLAY = pygame.display.set_mode( (W, H) )
pygame.display.set_caption('Maze runner')
font = pygame.font.Font('UbuntuMono-Bold.ttf', 24)
saidHello = False
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GOLD = (218, 165, 32)
run = True
rows = [[0 for i in range(21)] for j in range(21)]
cols = [[0 for i in range(21)] for j in range(21)]
for i in range(21):
    for j in range(21):
        rows[i][j] = True
        cols[i][j] = True

def drawMaze( rows ):
    for i in range(21):
        for j in range(21):
            if rows[i][j] :
                pygame.draw.line( DISPLAY, GOLD, (j*20, i*20), ((j+1)*20, i*20), 1 )
                pygame.draw.line( DISPLAY, GOLD, (j*20, i*20), (j*20, (i+1)*20), 1 )
                pygame.display.update()


def helloMessage():
    text = font.render( "Hello !, Welcome to the Maze", True, GREEN, BLUE )
    textRect = text.get_rect()
    textRect.center = ( W//2, H//2 )
    DISPLAY.fill( (0, 0, 0) )
    DISPLAY.blit( text, textRect )
    pygame.display.update()
    time.sleep( 1 )

while( run ):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if not saidHello :
        helloMessage()
        saidHello = True
    drawMaze( rows )