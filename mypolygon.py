import turtle
import math
bob = turtle.Turtle()

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,r):
    sides = 500
    circum = 2*math.pi*r
    length = circum/sides
    for i in range(sides):
        t.fd(length)
        t.lt(360/sides)

def arc(t,r,angle):
    circum = 2*math.pi*r
    length = circum/100
    for i in range(100):
        t.fd(length)
        t.lt(360/100)

arc(bob,50,90)
#circle(bob,100)
#polygon(bob,20,20)


turtle.mainloop()