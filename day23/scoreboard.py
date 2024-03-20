from turtle import Turtle

ALIGN = 'center'
FONT = ('Gongster', 12, 'bold')

class Score(Turtle):
    
    def __init__(self, width, height):
        super().__init__()
        self.height = height
        self.width = width
        self.level = 1
        self.pu()
        self.color('#000000')
        self.hideturtle()
        self.teleport(-(self.width/2) + 40, self.height/2 - 25)
        self.write(f'Level: {self.level}', False, ALIGN, FONT)
        
    
    def updateLevel(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', False, ALIGN, FONT)
        
    def gameOver(self):
        self.teleport(0,0)
        self.write('GAME OVER', False, ALIGN, FONT)