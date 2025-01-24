import pgzrun
TITLE="Quiz"
WIDTH=1000
HEIGHT=800
#Drawing the boxes for selection
mbox=Rect(0,0,1000,100)
qbox=Rect(0,100,800,150)
tbox=Rect(825,100,150,150)
sbox=Rect(825,270,150,400)





def draw():
    screen.fill("black")
    screen.draw.filled_rect(mbox, "black")
    screen.draw.filled_rect(qbox, "dark blue")
    screen.draw.filled_rect(tbox, "dark blue")
    screen.draw.filled_rect(sbox, "dark red")

def update():
    pass






pgzrun.go()