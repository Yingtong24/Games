import pgzrun
import random

WIDTH=1000
HEIGHT=900
score=0
gover=False

#Actors
duck=Actor("duck.png")
bread=Actor("bread.png")

#Drawing the area
def draw():
    screen.blit("field.jpg", (0,0))
    bread.draw()
    duck.draw()
    screen.draw.text("Score: " + str(score), color="Black", topleft=(900,30))
    if gover:
        screen.fill("Red")
        screen.draw.text("Game Over, score " + str(score), color="Black", center=(500,450))

#Teleport the Bread
def teleport():
    bread.pos=random.randint(0,900), random.randint(0,800)
    
#Moving the Duck
def update():
    global score
    pass
    if keyboard.left:
        duck.x=duck.x-2
    elif keyboard.right:
        duck.x=duck.x+2
    elif keyboard.up:
        duck.y=duck.y-2
    elif  keyboard.down:
        duck.y=duck.y+2
    if duck.colliderect(bread):
        teleport()
        score=(score +1)

teleport()

#Game Over
def gameo():
    global gover
    gover=True

#60 Seconds
clock.schedule(gameo,60.0)












pgzrun.go()

















pgzrun.go()
