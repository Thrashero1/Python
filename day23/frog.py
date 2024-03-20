from turtle import Turtle

class Frog(Turtle):
    
    def __init__(self, width, height):
        super().__init__()
        self.height = height
        self.width = width
        self.createFrog()
        self.movement = 20
    
    def createFrog(self):
        self.shape('turtle')
        self.pu()
        self.color('green')
        self.teleport(0, (-self.height/2) + 20)
        self.setheading(90)
    
    def moveForward(self):
        new_y = self.ycor() + self.movement
        self.goto(0, new_y)
    
    def resetFrog(self):
        self.teleport(0, (-self.height/2) + 20)