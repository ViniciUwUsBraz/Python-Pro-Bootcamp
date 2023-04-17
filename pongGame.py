import turtle
import time
import random

class Paddle(turtle.Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1.4, 5)
        self.setpos((position))
        self.setheading(90)

    def Up(self):
        if self.ycor()<260:
            self.forward(35)

    def Down(self):
        if self.ycor()>-260:
            self.backward(35)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.randint(110,210))
        self.shapesize(1,1)
        self.speed=18

    def speed_up(self):
        self.speed+=1

    def move(self):
        self.forward(self.speed)

    def change_direction(self):
        self.setheading(360-self.heading())
        self.left(180+random.randint(0,40))

    def hit_wall(self):
        self.setheading(360-self.heading())

    def reset(self):
        self.setpos(0,0)
        self.setheading(random.randint(1,360))
        self.speed=18

class Score(turtle.Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.setpos(position)
        self.pendown()

    def draw_score(self):
        self.write(f"{self.score}",align="center",font=('Arial', 30))

    def score_add(self):
        self.score+=1

line = turtle.Turtle()
line.hideturtle()
line.penup()
line.pencolor("white")
line.setpos(0,-300)
line.setheading(90)

for i in range(30):
    line.forward(20)
    line.pendown()
    line.forward(20)
    line.penup()

ball = Ball()
p1= Paddle((-380,0))
p2= Paddle((370,0))
score1= Score((-30,255))
score2= Score((30,255))

screen= turtle.Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

screen.onkey(p1.Up,"Up")
screen.onkey(p1.Down,"Down")
screen.onkey(p2.Up,"w")
screen.onkey(p2.Down,"s")

score1.draw_score()
score2.draw_score()

while(1):
    time.sleep(0.1)
    screen.update()

    if ball.distance(p1)<40 or ball.distance(p2)<40:
        ball.speed_up()
        ball.change_direction()

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.hit_wall()

    if ball.xcor()<-400:
        score2.clear()
        score2.score_add()
        score2.draw_score()
        ball.reset()
    elif ball.xcor()>400:
        score1.clear()
        score1.score_add()
        score1.draw_score()
        ball.reset()

    ball.move()

screen.exitonclick()
