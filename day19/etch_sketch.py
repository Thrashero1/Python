import random as rand
from turtle import *

tim = Turtle()
screen = Screen()
screen.screensize(500, 500)

def moveforward():
    tim.fd(5)

def moveback():
    tim.bk(5)

def turnleft():
    tim.left(5)

def turnright():
    tim.right(5)


screen.listen()


screen.onkeypress(moveforward, 'w' )
screen.onkeypress(moveback, 's' )
screen.onkeypress(turnleft, 'a' )
screen.onkeypress(turnright, 'd' )

screen.onkey(screen.reset, 'space')




screen.exitonclick()