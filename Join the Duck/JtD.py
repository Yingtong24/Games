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
dot=0
cds=0
dot=0

#Adding Actors
def duckarmy():
    global st
    for i in range(td):
        duck=Actor("duck.png")
        duck.pos=random.randint(50,900), random.randint(50,800)
        ducks.append(duck)
    st=time.time()

#Draw
def draw():
    global tt
    screen.blit("pond.jpg",(0,0))
    count=1
    for i in ducks:
        i.draw()
        screen.draw.text(str (count), (i.pos[0], i.pos[1]+50))
        count+=1
    for line in lines:
        screen.draw.line(line[0], line[1], (255,207,248))
    if dot < td:
        tt=time.time()-st
        screen.draw.text("Time Taken: "+ (str(round (tt))), (10,10), fontsize=50)
    else:
        screen.draw.text("Time Taken: "+ (str(round (tt))), (10,10), fontsize=50)
def update():
    pass
duckarmy()

def on_mouse_down(pos):
    global dot, lines
    if dot < 10:
        if ducks[dot].collidepoint(pos):
            if dot > 0:
                lines.append((ducks[dot-1].pos, ducks[dot].pos))
            dot+=1
        else:
            lines=[]
            dot=0
            







pgzrun.go()
