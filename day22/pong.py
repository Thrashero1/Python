from turtle import Screen
import time
import paddle
import ball
import scoreboard

HEIGHT = 600
WIDTH = 1000
game_on = True



scr = Screen()
scr.setup(WIDTH, HEIGHT)
scr.bgcolor('#000000')
scr.listen()
scr.tracer(0)

score = scoreboard.Scoreboard(HEIGHT)
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
    time.sleep(ball.move_speed)
    ball.checkCollision()
    
    if int(ball.distance(pad1)) < 60 and ball.xcor() > pad1.xcor() - 20:
        ball.bounce()
    
    elif int(ball.distance(pad2)) < 60 and ball.xcor() < pad2.xcor() + 20:
        ball.bounce()
    
    ball.checkBoundries()
    
    if ball.xcor() < -WIDTH/2 + 10:
        print('oops right gone')
        score.updateScore('left')
    
    if ball.xcor() > WIDTH/2 - 10:
        print('oops left gone')
        score.updateScore('right')
    
    game_on = score.gameStatus()
    
    
scr.exitonclick()

