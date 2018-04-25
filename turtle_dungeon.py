import turtle
import random
import time
import tkinter as tk
from L_system import L_system


class Manager():
    def __init__(self, continueChance):
        self.contChance = continueChance
        self.count = 0
        self.scale = 1
        self.path = ""
        self.pathList = []
        self.stack = []
        
    def DrawInitialRoom(self, t):
        t.penup()
        t.backward(5 * manager.scale)
        t.pendown()
        t.color('green')
        t.begin_fill()
        t.right(90)
        t.forward(5 * manager.scale)
        t.left(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.forward(5 * manager.scale)
        t.left(90)
        t.end_fill()
        t.penup()
        t.color('white')
        t.forward(5 * manager.scale)
        manager.count += 1
        manager.path = manager.path + '^'

    def DrawFinalRoom(self, t):
        t.penup()
        t.backward(5 * manager.scale)
        t.pendown()
        t.color('red')
        t.begin_fill()
        t.right(90)
        t.forward(5 * manager.scale)
        t.left(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.forward(5 * manager.scale)
        t.left(90)
        t.end_fill()
        t.penup()
        t.color('white')
        t.forward(5 * manager.scale)
        manager.count += 1
        manager.path = manager.path + '#'
        
    def DrawRoom(self, t):
        t.penup()
        t.backward(5 * manager.scale)
        t.pendown()
        t.begin_fill()
        t.right(90)
        t.forward(5 * manager.scale)
        t.left(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.forward(10 * manager.scale)
        t.left(90)
        t.forward(5 * manager.scale)
        t.left(90)
        t.end_fill()
        t.penup()
        t.forward(5 * manager.scale)
        manager.count += 1
        manager.path = manager.path + 'f'

    def DrawShortCorridor(self, t):
        t.pendown()
        t.forward(30 * manager.scale)
        t.penup()
        manager.count += 1
        manager.path = manager.path + '1'

    def DrawLongCorridor(self, t):
        t.pendown()
        t.forward(60 * manager.scale)
        t.penup()
        manager.count += 1
        manager.path = manager.path + '2'

    def DecideDirection(self, t, n): # 2 for lr, 3 for lru
        x = random.random()
        if x <= self.contChance:
            return
        else:
            y = random.randrange(0, n) 
            if y == 0:
                t.right(90)
                self.path = self.path + 'R'
            elif y == 1:
                t.left(90)
                self.path = self.path + 'L'
            else:
                t.left(180)
                self.path = self.path + 'U'

    def RandomWalk(self, t):
        self.DrawInitialRoom(t)
        while(manager.count < 30):
            self.DrawLongCorridor(t)
            self.DecideDirection(t, 3)
        self.DrawFinalRoom(t)
    
    def PushToStack(self, t):
        state = (t.pos(), t.heading())
        self.stack.append(state)

    def PopFromStack(self):
        state = self.stack.pop()
        return state

    def MoveToPos(self, t):
        state = self.PopFromStack()
        t.setpos(state[0])
        t.seth(state[1])
        
    def DrawFromInput(self, t, in_str):
        print("Drawing from input")
        print(in_str)
        self.DrawInitialRoom(t)
        for ch in in_str:
            if ch == 'f':
                self.DrawRoom(t)
            elif ch == '^':
                self.DrawInitialRoom(t)
            elif ch == '#':
                self.DrawFinalRoom(t)
            elif ch == '1':
                self.DrawShortCorridor(t)
            elif ch == '2':
                self.DrawLongCorridor(t)
            elif ch == 'L':
                t.left(90)
            elif ch == 'R':
                t.right(90)
            elif ch == 'U':
                t.left(180)
            elif ch == 'u':
                t.left(180)
            elif ch == '[':
                self.PushToStack(t)
            elif ch == ']':
                self.MoveToPos(t)
            else:
                print("Unexpected input")

def Reset(this_screen, this_turtle):
    this_screen.reset()
    this_screen.bgcolor('black')
    this_turtle.color('white')
    this_turtle.pensize(4)
    this_turtle.ht()
    this_turtle.speed(0)

def SavePath():
    print(manager.path)
    manager.pathList.append(manager.path)
    manager.path = ""

#setup 
manager = Manager(0.5)
turtle.setup(1200, 800)
win = turtle.Screen()
win.screensize(3000, 3000)
alex = turtle.Turtle()

l_sys = L_system()

#initial
Reset(win, alex)
manager.RandomWalk(alex)

initialPath = manager.path
for i in range(0, 1):
    currentPath = ""
    Reset(win, alex)
    currentPath = l_sys.evolve(initialPath)
    manager.DrawFromInput(alex, currentPath)
    initialPath = currentPath
    time.sleep(5)
print("DONE")
