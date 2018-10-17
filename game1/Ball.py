import pygame, sys
from pygame.locals import *

pygame.init()
icon = pygame.image.load("tb01.png")
size = width, height = 1000, 600
FPS = 200
#设置帧数的方法
fclock = pygame.time.Clock()
speed = [4,1]
Black = 0,0,0
still = False
#设置游戏的分辨率
#设置屏幕可调节大小
#screen = pygame.display.set_mode(size,pygame.RESIZABLE)
screen = pygame.display.set_mode(size)
#设置屏幕无边框
#screen = pygame.display.set_mode(size,pygame.NOFRAME)

#设置标题
pygame.display.set_caption('ball game!')
#设置图标
pygame.display.set_icon(icon)
ball = pygame.image.load("ball.png")
#建立一个小球的矩形框，可以调用top，left,right,botton等方法
ballrect = ball.get_rect()
move_a, move_d, move_w, move_s = 0, 0, 0, 0
# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0])-1) * int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            #move方法控制小球的移动，两个参数表示水平和竖直
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        elif event.type ==pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                ballrect = ballrect.move(event.pos[0]-ballrect.left,event.pos[1] - ballrect.top)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left,event.pos[1] - ballrect.top)

    if pygame.display.get_active() :
        ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
        if ballrect.right > width and ballrect.right+speed[0] > ballrect.right:
            speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
            speed[1] = - speed[1]

    #填充颜色
    screen.fill(Black)
    #设置FPS
    fclock.tick(FPS)
    #让小球跟随框体移动
    screen.blit(ball,ballrect)
    #刷新
    pygame.display.update()
