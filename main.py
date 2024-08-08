import pygame
import random
import math
import time

pygame.init()


width=800
height=600
count=0
chance=3
level=1
x=1


screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("AIRSPACE")
bg=pygame.image.load('space.png')

#ROCKET
rocket=pygame.image.load('rocket.png')
rocketx=400
rockety=500
xchange=0

def Rocket(x,y):
    screen.blit(rocket, (x,y))


#UFO
ufo=[]
ufox=[]
ufoy=[]
ufoxch=[]
ufoych=[]
nos=6
speed=3

def ufospan(n,speed):


    for i in range(n):

        ufo.append(pygame.image.load('ufo1.png'))
        ufox.append(random.randint(0,740))
        ufoy.append(random.randint(0,300))
        ufoxch.append(speed)
        ufoych.append(0)

def Ufo(x,y,i):
    screen.blit(ufo[i], (x,y))

#BULLET
bulletst="ready"


bullet=pygame.image.load('bullet.png')
bulletx=400
bullety=500
bulletch=30

def Bullet(x,y):
    global bulletst
    bulletst="fire"
    screen.blit(bullet, (x + 17,y))


def collision(bulletx,bullety,ufox,ufoy):
    distance=math.sqrt((math.pow(ufox-bulletx,2)+(math.pow(ufoy-bullety,2))))
    if distance<28:
        return True
    else:
        return False


def collision2(rocketx, rockety, ufox, ufoy):
    distance2 = math.sqrt((math.pow(ufox - rocketx, 2) + (math.pow(ufoy - rockety, 2))))
    if distance2 <40:
        return True
    else:
        return False

#button stuff
start=pygame.image.load('start.jpg')
exit=pygame.image.load('exit.jpg')

Sx=start.get_width()
Sy=start.get_height()
Ex=exit.get_width()
Ey=exit.get_height()
rect=pygame.Rect(width//2 - 70,200,Sx,Sy)
rect1=pygame.Rect(width//2-70,300,Ex,Ey)
button2=pygame.transform.scale(start,(Sx-10,Sy-10))


#XTRA
score=0
flag=True
action=False
#ones=True
run=True
while(run):
    
    screen.fill((202, 255, 251))
    ufospan(nos, speed)

    screen.blit(start,(330,200))
    screen.blit(exit,(330,300))

    if(action):
        screen.blit(bg, (0, 0))

        #ufospan(n)

    

    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            run=False


        

        #START AND EXIT

        elif event.type == pygame.MOUSEBUTTONDOWN and action == False:
            if (rect.collidepoint(event.pos)):
                screen.fill((202, 230, 251))
                screen.blit(button2, (334,205))
                #time.sleep(0.20)
                pygame.display.flip()
                action = True
            elif(rect1.collidepoint(event.pos)):
                run=False



#Don't Touch daa

        if(action):
                #ROCKET CONTROL
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT or event.key == pygame.K_a:
                    xchange-=10
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    xchange +=10

                #BULLET CONTROL
                if event.key==pygame.K_SPACE or event.key == pygame.K_s:
                    bulletx=rocketx
                    Bullet(bulletx,bullety)

            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a:
                    xchange=0

    rocketx += xchange

    if bullety<=0:
        bullety=500
        bulletst="ready"

    #ufospan(nos,speed)

    if rocketx<=0:
        rocketx=0
    if rocketx>=740:
        rocketx=740

    if (bulletst == "fire"):
        bullety -= bulletch

        Bullet(bulletx, bullety)
    #UFO MOVEMENT
    if(action):
        Rocket(rocketx, rockety)
        for i in range(nos):
            ufox[i] += ufoxch[i]
            ufoy[i]+= ufoych[i]

            if ufox[i]>740:
                ufoxch[i]*=-1
                ufoych[i]+=0.5
            if ufox[i]<0:

                ufoxch[i]*=-1


            if collision(bulletx, bullety, ufox[i], ufoy[i]):
                bullety = 500
                bulletst = "ready"
                score += 1
                ufox[i] =400
                ufoy[i]= -80
                ufoxch[i]=0
                ufoych[i]=0
            #print(score)



            if collision2(rocketx, rockety, ufox[i], ufoy[i]):



                count+=1





                if count==1 :
                    screen.fill((0, 0, 0))
                    font1 = pygame.font.Font('freesansbold.ttf', 45)

                    text1 = font1.render("GAME OVER !", True, (255, 0, 0), (0, 0, 0))
                    textRect1 = text1.get_rect()
                    

                    textRect1.center = (width // 2, height // 2)
                    screen.fill((0,0,0))
                    screen.blit(text1, textRect1)
                    pygame.display.flip()
                    time.sleep(1.5)
                    screen.fill((0,0,0))
                    
                    run=False


            #LEVELS
            if score>=nos:
                    nos=nos*2

                    level+=1
                    speed+=3
                    ufoxch.append(speed)

                    font3 = pygame.font.Font('freesansbold.ttf', 45)

                    text3 = font3.render("LEVEL  " + str(level), True, (0, 0, 255))
                    textRect3 = text3.get_rect()

                    textRect3.center = (width // 2, height // 2)
                    if(level!=4):
    		
                        screen.blit(bg, (0,0))

                        screen.blit(text3, textRect3)
                        pygame.display.flip()
			

                        
                        time.sleep(0.5)


            Ufo(ufox[i], ufoy[i], i)

            if(level>3):
                font4 = pygame.font.Font('freesansbold.ttf', 16)

                text4 = font4.render("YOU REACHED THE MAXIMUM LEVEL,STAY TUNED FOR NEXT UPDATE :)", True, (255,255, 255))
                textRect4 = text4.get_rect()

                textRect4.center = (width // 2, height // 2)
                screen.blit(bg, (0,0))
                screen.blit(text4, textRect4)
                pygame.display.flip()
                time.sleep(0.19)

                run=False

            #Ufo(ufox[i], ufoy[i], i)
#score
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render("YOUR SCORE " + str(score), True, (255,95,21))
    textRect = text.get_rect()
    textRect.center = (100, 30)

    screen.blit(text,textRect)


    #screen.fill((255,255,255))
    pygame.display.update()

pygame.quit()






     

              
