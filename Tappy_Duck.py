import pgzrun, random
WIDTH=1000
HEIGHT=700
#Title for the window (Top left)
TITLE="Tappy Duck"
duck=Actor("duck.png")
message=""
#Importing the duck
def draw():
    screen.fill("Light Blue")
    duck.draw()
    screen.draw.text(message,center = (900, 50), fontsize=30)
def move():
    duck.x=random.randint(0, 1000)
    duck.y=random.randint(0,700)
#Clicking the duck
def on_mouse_down(pos):
    global message
    if duck.collidepoint(pos):
        message="Yay :)!"
        move()
    else:
        message=" Noo :("






pgzrun.go()