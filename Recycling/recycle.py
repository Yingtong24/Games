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
    global items, lv1
    if len(items) == 0:
        items=objects(lv1)

def objects(extra):
    newitems=[]
    options=["paperbag.png"]+random.choice(ITEMS, k=extra)
    random.shuffle(options)
    for i in options:
        item=Actor(i)
        newitems.append(item)
        gap_size = WIDTH / (len(newitems) +1)
        #Len is to find the number of items
    for index, item in enumerate(newitems):
        item.x = (index + 1)*gap_size
        item.y = 0
        animate(item, duration = speed - lv1, y = HEIGHT)
    return newitems

def gameover():
    global gover
    gover=True

def on_mouse_down(pos):
    global items, lv1, lvs, gc
    for item in items:
        if item.collidepoint(pos):
            if "paperbag" in item.image:
                if lv1 == lvs:
                    gc=True
                else:
                    lv1+=1
                    items.clear
            else:
                gameover()
            









pgzrun.go()
