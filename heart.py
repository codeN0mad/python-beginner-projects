
import math
from turtle import Screen,Turtle

def hearta(K):
    return 15 * math.sin(K)

def heartb(k):
    return 11.8*math.cos(k) - 5 * math.cos(2 * k) - 2*math.cos(3 * k) - math.cos(4 * k)

screen = Screen()
screen.bgcolor("black")


t = Turtle()
t.speed(0)
t.color("red")
t.penup()

for i in range (10000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    t.goto(x, y)
    for j in range(3):
        t.goto(x,0)
        t.color("red")
    t.pendown()

screen.mainloop()


