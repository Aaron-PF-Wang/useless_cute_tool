#点击空格抛硬币
import pygame,sys,math,random
#def cos(len):return math.cos(math.radians(len))
def cos(n):#这里cos函数可以是任意的，个人感觉线性的看着更舒服
    if 0<=n<=180:
        return -n/90+1
    elif n>180:
        return -cos(n-180)
    else:
        return -cos(n+180)
def drawCoin(height,length,towards,high,time,position,coin):
    Px=position[0]-25
    color=[[(192,192,192),(142,142,142)],['yellow',(150,150,0)]][coin[1]]
    for i in range(1,101):
        pygame.draw.ellipse(screen,(150,150,0),(Px,position[1]-25+i*0.25*length+high,50,50*height))
    if towards>0:
        pygame.draw.ellipse(screen,color[0],(Px,position[1]-25+high,50,50*height))
    if towards<=0:
        pygame.draw.ellipse(screen,color[0],(Px,position[1]-25+high+length*25,50,50*height))
    if time==30:
        coin[1]=random.randint(0,1)
pygame.init()
screen = pygame.display.set_mode((300, 300))
animate=False
T=0
time=54
clock = pygame.time.Clock()
high=0
speed=0
coin=[1,1]
while True:
    T=T+1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if pygame.key.get_pressed()[pygame.K_SPACE] and not animate:
        animate=True
        time=-6
        high=0
        speed=5

    screen.fill((255,255,255))

    if animate:
        high-=speed
        if (time>-15 and time<0)or(time>15 and time<30)or(time>45 and time<60):towards=1
        else:towards=-1
        drawCoin(abs(cos((time-15)*6))+0.02,(1-cos((time-15)*12))/3,towards,high,time,[150,150],coin)
        speed-=1/6
        time+=1
    else:
        drawCoin(0.5,0.5,1,0,time,[150,150],coin)


    clock.tick(60)
    pygame.display.flip()
    if time==54:
        animate=False
