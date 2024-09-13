import pgzrun, random
WIDTH=1000
HEIGHT=700
def draw():
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    radius=(50)
    screen.clear()
    for i in range(20):
        red=random.randint(0,255)
        green=random.randint(0,255)
        blue=random.randint(0,255)

        screen.draw.circle((400,300),radius,(red,green,blue))
        radius+=10
pgzrun.go()