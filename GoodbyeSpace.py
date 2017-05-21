'''
    Significant help from https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python
    Modified for my goals
    
    move and fire with arrow keys
    '''

# 1 - Import library
import pygame
import math
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
playerpos=[width//2-22,height-45]
invaders=[[30,10],[130,10],[230,10],[330,10],[430,10],[530,10]]
left = True
down = False
acc=[0,0]
bullets=[]


# 3 - Load images
player = pygame.image.load("resources/defense.png")
space = pygame.image.load("resources/space.png").convert()
ground = pygame.image.load("resources/ground.png").convert()
invaderimg = pygame.image.load("resources/invader.png")
bulletimg = pygame.image.load("resources/bullet.png").convert()

# 4 - keep looping through
while 1:
    
    # Draw Background
    screen.fill(0)                                      # clears the screen
    
    for x in range(width//space.get_width()+1):         # background
        for y in range(height//space.get_height()+1):
            screen.blit(space,(x*300,y*300))
    
    for x in range(width//ground.get_width()+1):        # planet
        screen.blit(ground,(x*300,height-40))


    # Place and Draw Invader
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
    
        badrect = pygame.Rect(invaderimg.get_rect())
        badrect.top = invader[1]
        badrect.left = invader[0]
#        if badrect.left < 64:
#            hit.play()
#            healthvalue -= random.randint(5,20)
#            invaders.pop(index)

        # move down one if you're at the edge
        if down == True:
            invader[1]+=30
            down = False
        index+=1

        screen.blit(invaderimg, invader)

    # 6.2 - Draw bullet
    for bullet in bullets:
        index=0
        velocity = 3
        bullet[1]-=velocity
        if bullet[0]<0:
            bullets.pop(index)
            playerpos[0] += 100     # doesn't seem to be working :(
        index+=1
        screen.blit(pygame.transform.rotate(bulletimg, 0), (bullet[0], bullet[1]))

    # 6.1 - Draw player
    screen.blit(player, playerpos)

    # 6.3.2 - Check for collisions
    for bullet in bullets:
        bullrect=pygame.Rect(bulletimg.get_rect())
        bullrect.left=bullet[0]
        bullrect.top=bullet[1]

        for invader in invaders:
            badrect = pygame.Rect(invaderimg.get_rect())
            badrect.top = invader[1]
            badrect.left = invader[0]
            # this is backwards from before, suggeting that one is wrong.
            # but which one? we'll never know...

            if badrect.colliderect(bullrect):
                acc[0]+=1
                invaders.remove(invader)
                bullets.remove(bullet)

    # 7 - update the screen
    pygame.display.update()

    # 8 - dealing with key presses
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            # not sure what this does, but looks important
            pygame.quit()
            exit(0)
        
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                # fires a bullet
                acc[1]+=1
                bullets.append([playerpos[0]+19,playerpos[1]])
            if event.key==K_x:
                # quits the game
                pygame.quit()
                exit(0)

    # moving back and forth
    # treated differently, becasue can hold down key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: playerpos[0]-=5
    if keys[pygame.K_RIGHT]: playerpos[0]+=5



#    pygame.key.set_repeat(500,500)






