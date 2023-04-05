import random
import turtle

colors=["blue","red","green","yellow","pink"]

aux=0
x=-200
y=-60
turtles=[]
winner=[]
lose=False
for t in range(5):
    t=turtle.Turtle()
    turtles.append(t)

screen=turtle.Screen()
screen.setup(500,400)

for t in turtles:
    t.shape("turtle")
    t.color(colors[aux])
    aux+=1
    t.penup()
    t.setpos(x,y)
    y+=30
    t.pendown()

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race?")

while(turtles[0].xcor()<100 and turtles[1].xcor()<100 and turtles[2].xcor()<100 and turtles[3].xcor()<100 and turtles[4].xcor()<100 ):
    for t in turtles:
        t.forward(random.randint(1,4))
        if t.xcor()>=100:
            print(f"{t.color()[0].title()} turtle wins")
            winner.append(t.color()[0])

for color in winner:
    if user_bet==color:
        print("Your bet was right!")

screen.exitonclick()