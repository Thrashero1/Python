from turtle import *    
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

snake = Snake(3)
food = Food()
score = Scoreboard()

height = 600
width = 600
scr = Screen()
scr.setup(height,width)
scr.bgcolor('#000000')
scr.tracer(0)
game_on = True
scr.title('SNAKE')


scr.listen()
scr.onkey(snake.goUp, 'Up')
scr.onkey(snake.goDown, 'Down')
scr.onkey(snake.goLeft, 'Left')
scr.onkey(snake.goRight, 'Right')


while game_on:
    scr.update()
    time.sleep(0.1)
    snake.move()
    if int(snake.head.distance(food)) < 9:
        food.moveFood()
        snake.increasesize()
        score.updateScore()

    game_on = snake.checkEdge(height, width)
    if game_on == False:
        score.gameOver()

    
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 5:
            game_on = False
            score.gameOver()




scr.exitonclick()


