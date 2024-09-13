import pgzrun, random
WIDTH=1000
HEIGHT=700
def draw():
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    w=800
    h=100
    screen.clear()
    for i in range(20):
        red=random.randint(0,255)
        green=random.randint(0,255)
        blue=random.randint(0,255)
        rec=Rect((0,0),(w,h))
        rec.center=500,350
        screen.draw.rect(rec,(red,green,blue))
        w-=10
        h+=10






























pgzrun.go()