import pgzrun
import random
WIDTH=1000
HEIGHT=850
#Variables
lvs=5
speed=10
gover=False
gc=False
lv1=1
items=[]
ITEMS=["battery.png", "chemical.png", "fire.png", "plasticbag.png"]

def draw():
    screen.blit("background.jpg", (0,0))
        
def update():
    pass
def objects(extra):
    newitems=[]
    options=["paperbag.png"]+random.choice(ITEMS, k=extra)
    random.shuffle(options)
    for i in options:
        item=Actor(i)
        newitems.append(item)
        gap_size = WIDTH / (len(newitems) +1)
        #Len is to find the number of items




























pgzrun.go()
