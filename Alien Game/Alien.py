import pgzrun, random
WIDTH=1000
HEIGHT=700
#Title for the window (Top left)
TITLE="Beat The Alien"
alien=Actor("alien.jpg")
message="Hello"
#Importing the Alien
def draw():
    screen.fill("Dark Blue")
    alien.draw()
    screen.draw.text(message,center = (900, 50), fontsize=30)
def move():
    alien.x=random.randint(0, 1000)
    alien.y=random.randint(0,700)
#Tapping the Alien
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="Goal!"
        move()
    else:
        message=" ^*&^*&%^&^"






pgzrun.go()