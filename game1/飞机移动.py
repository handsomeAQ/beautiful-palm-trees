#载入pygame和sys 导入包，sys模块负责程序与Pygame解释器的交互，用于操控Pygame的运行时的环境
import pygame, sys
import time
from pygame.locals import *

#第二部分：
#初始化pygame
pygame.init()
#设置suface对象 屏幕分辨率
FPS = 60
screen = pygame.display.set_mode((412,535))

background = pygame.image.load('1.jpg').convert()

hero = pygame.image.load('./sc/image/hero1.png')
#坐标
x = 160
y = 435
#设置背景图片
screen.blit(background,(0,0))
#飞机显示
screen.blit(hero,(x,y))
move_a, move_d, move_w, move_s = 0, 0, 0, 0
#设置窗口名称
pygame.display.set_caption('hello World!')

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                move_a = 1
            elif event.key == K_d or event.key == K_RIGHT:
                move_d = 1
            elif event.key == K_UP or event.key == K_w:
                move_w = 1
            elif event.key == K_DOWN or event.key == K_s:
                move_s = 1
            elif event.key == K_SPACE:

        elif event.type == KEYUP:
            # 某一个方向的键盘被松开，这个方向的偏移量赋为0
            if event.key == K_a or event.key == K_LEFT:
                move_a = 0
            elif event.key == K_d or event.key == K_RIGHT:
                move_d = 0
            elif event.key == K_UP or event.key == K_w:
                move_w = 0
            elif event.key == K_DOWN or event.key == K_s:
                move_s = 0
    x = x + move_d - move_a
    y = y + move_s - move_w

            #pygame.display控制屏幕
    screen.blit(background, (0, 0))
    screen.blit(hero, (x, y))
    pygame.display.update()
        #延时
    time.sleep(0.01)
