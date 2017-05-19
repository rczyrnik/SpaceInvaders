'''
    Significant help from https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python
    Modified for my goals
    
    "a" = move left
    "d" = move right
    "f" = fire
    '''

# 1 - Import library
import pygame
import math
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False]
playerpos=[width//2-22,height-45]
invaders=[[30,10],[130,10],[230,10],[330,10],[430,10],[530,10]]
left = True
down = False
acc=[0,0]
arrows=[]

# 3 - Load images
player = pygame.image.load("resources/defense.png")
space = pygame.image.load("resources/space.png")
ground = pygame.image.load("resources/ground.png")
invaderimg = pygame.image.load("resources/invader.png")
arrow = pygame.image.load("resources/bullet.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    
    # 6 - draw the screen elements
    for x in range(width//space.get_width()+1):         # background
        for y in range(height//space.get_height()+1):
            screen.blit(space,(x*300,y*300))
    
    for x in range(width//ground.get_width()+1):        # planet
        screen.blit(ground,(x*300,height-40))

    for invader in invaders:                            # invaders
        screen.blit(invaderimg, invader)


    #updates y position of the invader, removes if off screen
    index=0

    for invader in invaders:
        if invader[1] > (height-80):
            invaders.pop(index)
        
        # move left or right each round
        if invader[0]%100 == 60:
            left = False
            down = True
        if invader[0]%100 == 0:
            left = True
            down = True

        if left == True:
            invader[0]+=1
        else:
            invader[0]-=1
    
        # move down one if you're at the edge
        if down == True:
            invader[1]+=30
            down = False
        index+=1


    # 6.2 - Draw bullet
    for bullet in arrows:
        index=0
        velocity = 3
        bullet[2]-=velocity
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))


    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()
    angle = 0
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)



    # 7 - update the screen
    pygame.display.flip()



    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
    if event.type == pygame.KEYDOWN:
        if event.key==K_a:
            keys[0]=True
        elif event.key==K_d:
            keys[1]=True
        elif event.key==K_f:
            keys[2]=True

    if event.type == pygame.KEYUP:
        if event.key==pygame.K_a:
            keys[0]=False
        elif event.key==pygame.K_d:
            keys[1]=False
        elif event.key==pygame.K_f:
            keys[2]=False


    # 9 - Move player
    if keys[0]:
        playerpos[0]-=5
    if keys[1]:
        playerpos[0]+=5
    if keys[2]:
        position=pygame.mouse.get_pos()
        acc[1]+=1
        arrows.append([0,playerpos1[0]+15,playerpos1[1]-15])




