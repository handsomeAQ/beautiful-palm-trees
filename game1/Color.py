import pygame, sys
from pygame.locals import *

pygame.init()

#设置窗口
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('画画')

#设置颜色
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#在surface上画画
#将背景设置为白色
screen.fill(white)
#画出多边形
pygame.draw.polygon(screen,green,((146,0),(291,106),(236,277),(56,277),(0,106)))
#直线
pygame.draw.line(screen,blue,(60,60),(120,60),4)
pygame.draw.line(screen,blue,(120,60),(60,120),4)
pygame.draw.line(screen,blue,(60,120),(120,120),4)
#圆
pygame.draw.circle(screen,blue,(300,50),20,0)
#椭圆
pygame.draw.ellipse(screen,red,(300,250,40,80),1)
#矩形
pygame.draw.rect(screen,red,(200,150,100,50))

#设置单个像素点的颜色
pixObj = pygame.PixelArray(screen)
pixObj[480][380] = black
pixObj[482][382] = black
pixObj[484][384] = black
pixObj[486][386] = black
pixObj[488][388] = black
del pixObj

#run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#刷新
    pygame.display.update()