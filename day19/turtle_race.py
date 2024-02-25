import random as rand
from turtle import *
screen = Screen()
colours = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
turtles = ['timred', 'timblue', 'timgreen', 'timyellow', 'timpurple', 'timorange']
turtle_objects = []
screen.setup(500, 500)

winner = screen.textinput('Turtle Racing!', 'Which colour do you think will win?')

for x, y in enumerate(turtles):
    y = Turtle()
    y.shape('turtle')
    y.color(colours[x])
    y.speed(6)
    y.pu()
    turtle_objects.append(y)

def start_positions(turtle_list):
    space = 500 / 7
    start_y = 250 - space
    for turtle in turtle_list:
        turtle.teleport(-240, start_y)
        start_y -= space
        


def moveturtles(turtle_list):
    for turtles in enumerate(turtle_list):
        move = rand.randint(1, 300)
        turtles.fd(move)

for x in range(1,10):
    moveturtles(turtle_objects)

start_positions(turtle_objects)
screen.exitonclick()
