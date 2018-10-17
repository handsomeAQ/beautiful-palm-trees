#载入pygam和sys 导入包
import pygame, sys
from pygame.locals import *

#第二部分：
pygame.init()
FPS = 15
speed = [5,0]
red = (255,0,0)
width = 1200
height = 300
fpsClock = pygame.time.Clock()
#设置suface对象 屏幕分辨率
screen = pygame.display.set_mode((width,height))
#设置窗口名称
pygame.display.set_caption('Running Rubbit!')
white = (255,255,255)

Rubbit = pygame.image.load('rubbit.png')
RubbitRect = Rubbit.get_rect()
RubbitX = 10;
RubbitY = 10;
dir = 'right'
while True: # main game loop
    screen.fill(white)
    pygame.draw.rect(screen,red,(400,0,40,150))
    RubbitRect = RubbitRect.move(speed[0],speed[1])
    if RubbitRect.right >= 400:
       speed[0] = -speed[0];
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(Rubbit, (RubbitRect))
    pygame.display.update()
    fpsClock.tick(FPS)
