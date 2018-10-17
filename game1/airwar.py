#载入pygam和sys 导入包
import pygame, sys
from pygame.locals import *

#第二部分：
pygame.init()
FPS = 30
width = 640
height = 480
respeed = 8
boxsize = 40
gapsize = 10
boardwidth = 10
boardheight = 7
assert (boardheight * boardwidth) % 2 == 0
XMARGIN = int(width-(boardwidth*(boxsize + gapsize)) / 2)
YMARGIN = int(height-(boardheight*(boxsize + gapsize)) / 2)

#           R   G   B
GRAY     =(100, 100, 100)
NAVYBLUE =(60,   60, 100)
WHILE    =(255, 255, 255)
RED      =(255,   0,   0)
GREEN    =(0,   255,   0)
BLUE     =(0,     0, 255)
YELLOW   =(255, 255,   0)
ORANGE   =(255, 128,   0)
PURPLE   =(255,   0, 255)
CYAN     =(0,   255, 255)
bgcolor = NAVYBLUE
lightbgcolor = GRAY
boxcolor = WHILE
highlightcolor = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLOR = (RED,GREEN,BLUE,YELLOW,ORANGE,PURPLE,CYAN)
ALLSHAPES = (DONUT,SQUARE,DIAMOND,LINES,OVAL)
assert len(ALLCOLOR) * len(ALLSHAPES) * 2 >= boardwidth * boardheight

def main():
    global FPSCLOCK,DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((width,height))

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    reveledBoxes = generateRevealedBoxesData(False)

    firstSelection = None
    DISPLAYSURF.fill(bgcolor)
    startGameAnimation(mainBoard

while True: # main game loop
    mouseClicked = False

    DISPLAYSURF.fill(bgcolor)
    drawBoard(mainBoard, revealedBoxes)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type ==MOUSEBUTTONUP :
            mousex, mousey = event.pos
            mouseClicked = True

    boxx, boxy = getBoxAtPixel(mousex,mousey)
    if boxx != None and boxy != None:
        if not revealedBoxes[boxx][boxy]:
            drawHighlightBox(boxx, boxy)
        if not revealedBoxes[boxx][boxy] and mouseClicked:


            #pygame.display控制屏幕
        pygame.display.update()
