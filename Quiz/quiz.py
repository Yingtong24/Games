import pgzrun
TITLE="Quiz"
WIDTH=1000
HEIGHT=800
#Drawing the boxes for selection
mbox=Rect(0,0,1000,100)
qbox=Rect(0,100,800,150)
tbox=Rect(825,100,150,150)
sbox=Rect(825,270,150,500)
obox1=Rect(20,270,320,220)
obox2=Rect(450,270,320,220)
obox3=Rect(20,550,320,220)
obox4=Rect(450,550,320,220)

#Variables
score=0
timer=15 
message=""
gover=False
qfile="questions.txt"
questions=[]
total=0
index=0
ansbox=[obox1, obox2, obox3, obox4]

def draw():
    screen.fill("black")
    screen.draw.filled_rect(mbox, "black")
    screen.draw.filled_rect(qbox, "dark blue")
    screen.draw.filled_rect(tbox, "dark blue")
    screen.draw.filled_rect(sbox, "dark red")
    screen.draw.filled_rect(obox1, "yellow")
    screen.draw.filled_rect(obox2, "yellow")
    screen.draw.filled_rect(obox3, "yellow")
    screen.draw.filled_rect(obox4, "yellow")
    screen.draw.textbox("Skip", sbox, color="black", angle=-90)
    screen.draw.textbox(question[0].strip(), qbox, color="white")
    ind=1
    screen.draw.textbox(str(timer), tbox, color="dark red")
    for i in ansbox:
        screen.draw.textbox(question[ind].strip(), i, color="black")
        ind+=1

def update():
    pass

def updatetime():
    global timer
    if timer>0:
        timer-=1
    else:
        gameo()

def readf():
    global total, questions
    file=open(qfile, "r")
    for i in file:
        questions.append(i)
        total+=1
    file.close()

def readq():
    global index
    index+=1
    return questions.pop(0).split(",")
def gameo():
    global gover, timer, question
    message=f"Game over!\nYou got {score} questions correct!"
    question=[message, "-", "-", "-", "-", 5]
    timer=0
    gover=True
def correct():
    global timer, question, questions, score
    score+=1
    if questions:
        question=readq()
        timer=15
    else:
        gameo()

def on_mouse_down(pos):
    index=1
    for i in ansbox:
        if i.collidepoint(pos):
            if index==int(question[5]):
                correct()
            else:
                gameo()
        index+=1

readf()
question=readq()

clock.schedule_interval(updatetime,1)

pgzrun.go()
