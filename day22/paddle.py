from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self, width, height, pos):
        super().__init__()
        self.width = width
        self.height = height
        self.pad = self.createself(pos)
    
    
    def createself(self, pos):
        self.shape('square')
        self.color('#ffffff')
        self.pu()
        self.resizemode("user")
        self.shapesize(5, 1, 1)
        
        if pos == 'right':
            x_pos = self.width/2 - 50
            self.teleport(x_pos, 0)
        else:
            x_pos = -(self.width/2) + 50
            self.teleport(x_pos, 0)
        
        return self

    def moveUp(self):
        if self.pad.ycor() <= (self.height/2) - 20:
            new_y = self.pad.ycor() + 10
            new_x = self.pad.xcor()
            self.pad.goto(new_x, new_y)
        
    def moveDown(self):
        if self.pad.ycor() >= -(self.height/2) + 20:
            new_y = self.pad.ycor() - 10
            new_x = self.pad.xcor()
            self.pad.goto(new_x, new_y)
