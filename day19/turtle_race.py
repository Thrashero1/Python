import random as rand
from turtle import *
screen = Screen()
colours = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
turtles = ['timred', 'timblue', 'timgreen', 'timyellow', 'timpurple', 'timorange']
turtle_objects = []
x_size = 700
y_size = 300
screen.setup(x_size, y_size)

race_going = False

winner = screen.textinput('Turtle Racing!', 'Which colour do you think will win?')

if winner:
    race_going = True

for x, y in enumerate(turtles):
    y = Turtle(shape = 'turtle')
    y.color(colours[x])
    y.speed(0)
    y.pu()
    turtle_objects.append(y)

def start_positions(turtle_list):
    space = y_size / 7
    start_y = (y_size/2) - space
    for turtle in turtle_list:
        turtle.teleport(-x_size/2 - 10, start_y)
        start_y -= space
        
start_positions(turtle_objects)

def moveturtles(turtle_list):
    for turtles in turtle_list:
        move = rand.randint(1, 10)
        turtles.fd(move)

while race_going:
    moveturtles(turtle_objects)
    for turtle in turtle_objects:
        if turtle.xcor() > x_size / 2 - 20:
            if winner == turtle.pencolor():
                print(f'You have won! {winner} is the race winner!')
            else:
                print(f'Oh no {turtle.pencolor()} has won the race, you did not win!')
            race_going = False


screen.exitonclick()
