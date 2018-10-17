#载入pygame和sys 导入包，sys模块负责程序与Pygame解释器的交互，用于操控Pygame的运行时的环境
import pygame, sys
import time
from pygame.locals import *

#第二部分：
#初始化pygame
pygame.init()
#设置suface对象 屏幕分辨率
screen = pygame.display.set_mode((412,535))
background = pygame.image.load('1.jpg')
screen.blit(background,(0,0))
#设置窗口名称
pygame.display.set_caption('hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            #pygame.display控制屏幕
        pygame.display.update()
        #延时
        time.sleep(0.01)
