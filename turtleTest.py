import turtle as t
import random

color=""
sides=3
angle=180
x=0

taruga= t.Turtle()

while(x<20):

    if sides==3:
        for i in range(sides):
            taruga.forward(20)
            taruga.left(angle/sides*2)
    elif sides==4:
        for i in range(sides):
            taruga.forward(20)
            taruga.left(angle/sides)
    else:
        for i in range(sides):
            taruga.forward(20)
            taruga.left(180-angle/sides)

    color=random.choice(["alice blue","antique white","aquamarine","azure","black","blue violet","chartreuse","cyan"])
    taruga.pencolor(color)
    sides+=1
    angle+=180
    x+=1

screen=t.Screen()
screen.exitonclick()