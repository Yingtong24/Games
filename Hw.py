import pgzrun
WIDTH=1500
HEIGHT=1000
def draw():
    d1=Rect((150,20), (500,480))
    d2=Rect((200,40), (550,490))
    d3=Rect((250,60), (600,500))
    d4=Rect((300,80), (650,510))
    screen.draw.rect(d1,(155,212,129))
    screen.draw.rect(d2,(184,221,158))
    screen.draw.rect(d3,(167,18,59))
    screen.draw.rect(d4,(136,40,127))

pgzrun.go()