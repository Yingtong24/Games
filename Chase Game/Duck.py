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
    duck.draw()
    bread.draw()
    screen.draw.text("Score: " + str(score), color="Black", topleft=(900,30))
def update():
    pass


















pgzrun.go()