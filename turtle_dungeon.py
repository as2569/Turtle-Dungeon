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

    def DecideDirection(self, t):
        x = random.random()
        if x <= self.contChance:
            return
        else:
            y = random.randrange(0, 3)
            if y == 0:
                t.right(90)
                self.path = self.path + 'r'
            elif y == 1:
                t.left(90)
                self.path = self.path + 'l'
            else:
                t.left(180)
                self.path = self.path + 'u'

    def RandomWalk(self, t):
        while(manager.roomCount < 50):
            rand = random.randrange(4, 7)
            for x in range(rand):
                self.DrawRoom(alex)
            self.DecideDirection(alex)
        
    def RandomDirection(self, t):
        x = random.random()
        if x <= 0.25:
            t.right(90)
        elif x <= 0.50:
            t.left(90)
        elif x <= 0.75:
            t.left(180)
        else:
            return

    def DrawFromInput(self, t, in_str):
        print("Drawing from input")
        print(in_str)
        self.DrawInitialRoom(t)
        for ch in in_str:
            if ch == 'f':
                self.DrawRoom(t)
            elif ch == 'l':
                t.left(90)
            elif ch == 'r':
                t.right(90)
            elif ch == 'u':
                t.left(180)
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

manager = Manager(0.5)
l_sys = L_system()
turtle.setup(1200, 800)
win = turtle.Screen()
win.screensize(2000, 2000)
alex = turtle.Turtle()

Reset(win, alex)

manager.DrawInitialRoom(alex)
manager.RandomWalk(alex)

SavePath()
Reset(win, alex)

iteration = l_sys.createSystem(1, manager.pathList[0])
manager.pathList.append(iteration)
manager.DrawFromInput(alex, manager.pathList[1])

