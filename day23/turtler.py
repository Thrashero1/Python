from turtle import Screen
import time
import frog
import scoreboard
import cars
from random import Random

WIDTH = 600
HEIGHT = 600
game_on = True

score = scoreboard.Score(WIDTH, HEIGHT)
frog = frog.Frog(WIDTH, HEIGHT)
scr = Screen()
scr.setup(WIDTH, HEIGHT)
scr.listen()
scr.tracer(0)
scr.onkeypress(frog.moveForward,'Up')
car = cars.Cars(WIDTH, HEIGHT)

while game_on:
    time.sleep(0.1)
    scr.update()
    if frog.ycor() >= HEIGHT/2 - 5:
        score.updateLevel()
        frog.resetFrog()
        car.increaseSpeed()
    
    car.createCar()
    car.moveCars()
    for car1 in car.allcars:
        if frog.distance(car1) < 20 and frog.ycor() <= car1.ycor() + 20 and frog.ycor() >= car1.ycor() -20:
            score.gameOver()
            game_on = False

scr.exitonclick()