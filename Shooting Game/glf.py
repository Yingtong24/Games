import pgzrun
import random
WIDTH=1000
HEIGHT=850
#Variables
color=(154, 245, 178)
speed=7
bullets=[]
enemies=[]
score=0
#Actors
gingy=Actor("gingy.png")
gingy.pos=()
lordf=Actor("lord_farquaad.png")
def draw():
    gingy.draw()
    lordf.draw()






pgzrun.go()