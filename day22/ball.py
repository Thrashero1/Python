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
        
    def ballMove(self):
        new_y = self.ycor() + self.x_move
        new_x = self.xcor() + self.y_move
        self.goto(new_x, new_y)
    
    
    def bounce(self):
        if self.ycor() + 10 == self.height/2:
            self.x_move = -10
        elif self.ycor() - 10 == -(self.height/2):
            self.x_move = 10
        
    def checkCollision(self):
        if self.ycor() + 10 == self.height/2 or self.ycor() - 10 == -(self.height/2):
            self.bounce()
