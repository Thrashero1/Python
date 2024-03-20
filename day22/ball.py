from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        super().__init__()
        self.shape('circle')
        self.pu()
        self.color('#ffffff')
        self.x_move = 10
        self.y_move = -10
        self.move_speed = 0.1
        
    def ballMove(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)
    
    
    def bounceWalls(self):
        if self.ycor() + 10 == self.height/2:
            self.y_move = -10
        elif self.ycor() - 10 == -(self.height/2):
            self.y_move = 10
    
    def bounce(self):
        print('bounce')
        if self.xcor() + 10 >= self.width/2 - 100:
            self.x_move = -10
            print('left')
        else:
            print('right')
            self.x_move = 10
        self.move_speed /= 1.2
        
    def checkCollision(self):
        if self.ycor() + 10 == self.height/2 or self.ycor() - 10 == -(self.height/2):
            self.bounceWalls()
    
    def checkBoundries(self):
        if self.xcor() > self.width/2 or self.xcor() < -self.width/2:
            print('ball gone')
            self.x_move *= -1
            self.teleport(0,0)
            self.x_move = 10
            self.y_move = -10
            self.move_speed = 0.1