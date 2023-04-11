import turtle
import random
import time

def up():
    if head.heading()!= 270:
        head.setheading(90)

def right():
    if head.heading() != 180:
        head.setheading(0)

def down():
    if head.heading() != 90:
        head.setheading(270)

def left():
    if head.heading() != 0:
        head.setheading(180)

def expand_body(x):
    b=turtle.Turtle()
    b.shape("square")
    b.color("white")
    b.penup()
    b.setpos(x)
    body.append(b)

def move_body():
    old=head.pos()
    head.forward(20)
    for b in range(1,len(body)):
        new=body[b].pos()
        body[b].setpos(old)
        old=new
    time.sleep(0.1)
    screen.update()

def new_fruit():
    x=random.randint(-14,14)
    y=random.randint(-14,14)
    pos=(x*20,y*20)
    fruit.setpos(pos)

def hit():
    for b in body:
        if head.distance(b)==0 and b!=head:
            return 1
        elif head.ycor()>=300 or head.ycor()<=-300 or head.xcor()>=300 or head.xcor()<=-300:
            return 1

fruit=turtle.Turtle()
fruit.color("red")
fruit.shape("circle")
fruit.penup()

head= turtle.Turtle()
body=[head]
head.shape("square")
head.color("white")
head.shapesize(1)
head.penup()
head.speed("slow")

screen=turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

expand_body((-20,0))
expand_body((-40,0))
screen.update()

game_over=turtle.Turtle()
game_over.hideturtle()
game_over.setpos(-100,0)
game_over.color("white")

score_count = turtle.Turtle()
score_count.hideturtle()
score_count.setpos(-30,280)
score_count.color("white")
score=0
score_count.write(f"Score:{score}", move=False, font=('Arial',10))

turtle.onkey(up, "Up")
turtle.onkey(right, "Right")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")

new_fruit()
run=1

while(run):

    move_body()
    if hit():
        run=0
        game_over.write("Game Over!!", move=False, font=('Arial',30))

    if head.distance(fruit)<10:

        score_count.clear()
        score+=1
        score_count.write(f"Score:{score}", move=False, font=('Arial', 10))

        fruit.clear()
        new_fruit()
        expand_body(body[len(body)-1].pos())

screen.exitonclick()