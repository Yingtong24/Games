import pgzrun
import random
import time
WIDTH=1000
HEIGHT=850

#Variables
ducks=[]
lines=[]
st=0
tt=0
td=10
cds=0

#Adding Actors
def duckarmy():
    global st
    for i in range(td):
        duck=Actor("duck.jpg")
        duck.pos=random.randint(10,990), random.randint(10,840)
        ducks.append(duck)
    st=time.time()

#Draw
def draw():
    screen.blit("pond.jpg",(0,0))
    for i in ducks:
        i.draw()
def update():
    pass
duckarmy()
pgzrun.go()