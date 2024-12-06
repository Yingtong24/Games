import pgzrun
import random
import time
WIDTH=1000
HEIGHT=850

#Variables
frogs=[]
lines=[]
st=0
tt=0
td=10
dot=0
cds=0
dot=0

#Adding Actors
def froggies():
    global st
    for i in range(td):
        frog=Actor("frog.png")
        frog.pos=random.randint(50,900), random.randint(50,800)
        frogs.append(frog)
    st=time.time()

#Draw
def draw():
    global tt
    screen.blit("lilypads.jpg",(0,0))
    count=1
    for i in frogs:
        i.draw()
        screen.draw.text(str (count), (i.pos[0], i.pos[1]+50))
        count+=1
    for line in lines:
        screen.draw.line(line[0], line[1], (0, 255, 68))
    if dot < td:
        tt=time.time()-st
        screen.draw.text("Time Taken ( •̀ ω •́ )✧: "+ (str(round (tt))), (10,10), fontsize=50)
    else:
        screen.draw.text("Time Taken ( •̀ ω •́ )✧: "+ (str(round (tt))), (10,10), fontsize=50)
def update():
    pass
froggies()

def on_mouse_down(pos):
    global dot, lines
    if dot < 10:
        if frogs[dot].collidepoint(pos):
            if dot > 0:
                lines.append((frogs[dot-1].pos, frogs[dot].pos))
            dot+=1
        else:
            lines=[]
            dot=0


pgzrun.go()