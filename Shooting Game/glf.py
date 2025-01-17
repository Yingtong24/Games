import pgzrun
import random
WIDTH=1388
HEIGHT=850
#Variables
color=(154, 245, 178)
speed=7
bullets=[]
enemies=[]
score=0
#Actors
gingy=Actor("gingy.png")
gingy.pos=(694,750)
lordf=Actor("lord_farquaad.png")
lordf.pos=random.randint(50,1338), 100
shrek=Actor("shrek.png")
shrek.pos=random.randint(50,1338), 300
def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullet.png"))
        bullets[-1].x = gingy.x
        bullets[-1].y = gingy.y

def draw():
    screen.blit("castle.jpg", (0,0))
    gingy.draw()
    lordf.draw()
    shrek.draw()
    for i in bullets:
        i.draw()
    screen.draw.text("Score:"+str(score), (10,10), fontsize=30)

def update():
    global score
    pass
    if keyboard.left:
        gingy.x -= 10
        if gingy.x<0:
            gingy.x=0
    elif keyboard.right:
        gingy.x += 10
        if gingy.x>1388:
            gingy.x=1388
    lordf.y += 5
    if lordf.y>850:
        lordf.y=0
        lordf.x=random.randint(0,1388)
    for i in bullets:
        if i.y <=0:
            bullets.remove(i)
        else:
            i.y -= 20
    for i in bullets:
        if lordf.colliderect(i):
            score+=1
            bullets.remove(i)
            lordf.y=0
            lordf.x=random.randint(0,1388)

    shrek.y += 7
    if shrek.y>850:
        shrek.y=0
        shrek.x=random.randint(0,1388)
    for i in bullets:
        if i.y <=0:
            bullets.remove(i)
        else:
            i.y -= 20
    for i in bullets:
        if shrek.colliderect(i):
            score+=2
            bullets.remove(i)
            shrek.y=0
            shrek.x=random.randint(0,1388)
    
pgzrun.go()
