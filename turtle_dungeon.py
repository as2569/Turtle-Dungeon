import turtle
import random

class Manager():
    def __init__(self, continueChance, scale):
        self.contChance = continueChance
        self.roomCount = 0
        self.scale = scale
        self.path = ""

    def DrawInitialRoom(self, t):
        t.penup()
        t.forward(10 * manager.scale)
        t.pendown()
        #print(t.pos())
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
        #print(t.pos())
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
        manager.mainPath = manager.path + 'f'

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

manager = Manager(0.8, 0.5)
turtle.setup(1200, 800)
win = turtle.Screen()
win.bgcolor('black')
win.screensize(5000, 5000)
alex = turtle.Turtle()
alex.speed('fastest')
alex.pensize(4)
alex.ht()
alex.color('white')

manager.DrawInitialRoom(alex)
while(manager.roomCount < 100):
    manager.DrawRoom(alex)
    DecideDirection(alex)
    #RandomDirection(alex)

print(manager.path)


