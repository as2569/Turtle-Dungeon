import turtle
import random
from L_system import L_system

class Manager():
    def __init__(self, continueChance):
        self.contChance = continueChance
        self.roomCount = 0
        self.scale = 0.5
        self.path = ""
        self.pathList = []

    def DrawInitialRoom(self, t):
        t.penup()
        t.forward(10 * manager.scale)
        t.pendown()
        t.begin_fill()
        t.right(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.forward(20 * manager.scale)
        t.left(90)
        t.forward(20 * manager.scale)
        t.left(90)
        t.forward(20 * manager.scale)
        t.left(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.end_fill()
        t.penup()
        t.forward(10 * manager.scale)
        manager.roomCount += 1
        
    def DrawRoom(self, t):
        t.penup()
        t.forward(10 * manager.scale)
        t.pendown()
        t.forward(25 * manager.scale) #door
        t.begin_fill()
        t.right(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.forward(20 * manager.scale)
        t.left(90)
        t.forward(20 * manager.scale)
        t.left(90)
        t.forward(20 * manager.scale)
        t.left(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.end_fill()
        t.penup()
        t.forward(10 * manager.scale)
        manager.roomCount += 1
        manager.path = manager.path + 'f'

def DecideDirection(t):
    x = random.random()
    if x <= manager.contChance:
        return
    else:
        y = random.randrange(0, 2)
        if y == 0:
            t.right(90)
            manager.path = manager.path + 'r'
        else:
            t.left(90)
            manager.path = manager.path + 'l'

def RandomDirection(t):
    x = random.random()
    if x <= 0.25:
        t.right(90)
    elif x <= 0.50:
        t.left(90)
    elif x <= 0.75:
        t.left(180)
    else:
        return

def DrawFromInput(t, in_str):
    print("Drawing from input")
    print(in_str)
    manager.DrawInitialRoom(t)
    for ch in in_str:
        if ch == 'f':
            manager.DrawRoom(t)
        elif ch == 'l':
            t.left(90)
        elif ch == 'r':
            t.right(90)
        else:
            print("Unexpected input")

def Reset(this_screen, this_turtle):
    this_screen.reset()
    this_screen.bgcolor('black')
    this_turtle.color('white')
    this_turtle.pensize(4)
    this_turtle.ht()
    this_turtle.speed('fastest')

def SavePath():
    print(manager.path)
    manager.pathList.append(manager.path)
    manager.path = ''
    
manager = Manager(0.8)

turtle.setup(1200, 800)
win = turtle.Screen()
win.screensize(3000, 3000)
alex = turtle.Turtle()

Reset(win, alex)

manager.DrawInitialRoom(alex)
while(manager.roomCount < 25):
    manager.DrawRoom(alex)
    DecideDirection(alex)
    #RandomDirection(alex)

SavePath()
Reset(win, alex)

l_sys = L_system()
iteration = l_sys.createSystem(1, manager.pathList[0])
manager.pathList.append(iteration)
DrawFromInput(alex, manager.pathList[1])

