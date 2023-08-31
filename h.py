import time

import pygame

pygame.init()

width=800
height=600
count=0


screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("sample game")
bg=pygame.image.load('space.png')
button=pygame.image.load('button1.jpg')
x=button.get_width()
y=button.get_height()
action=False
rect=pygame.Rect(330,200,x,y)
button2=pygame.transform.scale(button,(x-10,y-10))
run=True

i=0
while(run):
    screen.fill((202, 230, 251))
    screen.blit(button, (330,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type==pygame.MOUSEBUTTONDOWN and action==False:
            if (rect.collidepoint(event.pos)):
                screen.fill((202, 230, 251))
                screen.blit(button2,(334,205))
                print(i)
                i+=1
                time.sleep(0.25)
                pygame.display.flip()

    pygame.display.update()

pygame.quit()