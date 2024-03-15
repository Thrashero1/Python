from turtle import Screen
import time
import paddle
import ball

HEIGHT = 600
WIDTH = 800
game_on = True

scr = Screen()
scr.setup(WIDTH, HEIGHT)
scr.bgcolor('#000000')
scr.listen()
scr.tracer(0)

ball = ball.Ball(WIDTH, HEIGHT)
pad1 = paddle.Paddle(WIDTH, HEIGHT, 'right')
pad2 = paddle.Paddle(WIDTH, HEIGHT, 'left')

scr.onkeypress(pad1.moveUp,'Up')
scr.onkeypress(pad1.moveDown, 'Down')

scr.onkeypress(pad2.moveUp,'w')
scr.onkeypress(pad2.moveDown, 's')


while game_on:
    scr.update()
    ball.ballMove()
    time.sleep(0.05)
    ball.checkCollision()
    
scr.exitonclick()

