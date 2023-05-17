import random
import time
from turtle import Turtle, Screen

class Finish(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pensize(3)

    def draw(self,x):
        self.setpos(x)
        for i in range(120):
            if i%2==0:
                self.penup()
            else:
                self.pendown()
            self.forward(5)
        self.penup()

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-280,280)
        self.lvl=1

    def stage(self):
        self.setpos(-280, 260)
        self.clear()
        self.write(f"Stage {self.lvl}",True,font=('Arial', 16, 'normal'))

    def stage_pass(self):
        self.lvl+=1
        self.setpos(0,0)
        self.write(f"Stage Complete",True, align='center', font=('Arial', 30, 'normal'))

    def game_over(self):
        self.setpos(0,0)
        self.write(f"GAME OVER!!",True, align='center', font=('Arial', 30, 'normal'))

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setpos(0,-280)
        self.setheading(90)

    def Up(self):
        self.setheading(90)
        self.forward(10)

    def Down(self):
        self.setheading(270)
        self.forward(10)

    def Left(self):
        self.setheading(180)
        self.forward(10)

    def Right(self):
        self.setheading(360)
        self.forward(10)

    def reset_pos(self):
        self.setpos(0,-280)

    def hit(self):
        for i in cars.cars:
            if self.distance(i)<14:
                return True

colors=["red","blue","pink","yellow","purple","green"]
class Cars():

    def __init__(self):
        self.speed=6
        self.cars=[]

    def new_car(self):
        car = Turtle("square")
        car.shapesize(1,2)
        car.penup()
        car.color(random.choice(colors))
        car.setpos(-300,random.randint(-240,240))
        self.cars.append(car)

    def move(self):
        for i in self.cars:
            i.forward(self.speed)

    def stage_pass(self):
        for i in self.cars:
            i.setpos(0,330)
        self.speed += 2

screen = Screen()
screen.setup(600,600)
screen.tracer(0)

player = Player()
cars = Cars()
score = Score()
finish = Finish()

screen.listen()
screen.onkey(player.Up,"Up")
screen.onkey(player.Down,"Down")
screen.onkey(player.Left,"Left")
screen.onkey(player.Right,"Right")

game=True
finish.draw((-300,250))
finish.draw((-300,-250))

while game:
    time.sleep(0.1)

    if random.randint(1,2)==1:
        cars.new_car()

    score.stage()
    screen.update()
    cars.move()

    if player.hit():
        score.game_over()
        game=False

    if player.ycor()>=250:
        score.stage_pass()
        cars.stage_pass()
        player.reset_pos()
        time.sleep(2)

screen.exitonclick()

