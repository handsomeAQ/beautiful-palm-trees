#载入pygam和sys 导入包
import pygame, sys
from pygame.locals import *

#第二部分：
pygame.init()
#设置suface对象 屏幕分辨率
screen = pygame.display.set_mode((400,300))
#设置窗口名称
pygame.display.set_caption('hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN]:","#",event.key,event.mod)
            else:
                print("[KEYDOWN]:", event.unicode, event.key, event.mod)

        elif event.type == pygame.MOUSEMOTION:
                print("[MOUSEMOTION]", event.pos, event.rel, event.buttons)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("[MOUSEBUTTONUP]", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MOUSEBUTTONDOWN]", event.pos, event.button)
            #pygame.display控制屏幕
        pygame.display.update()
