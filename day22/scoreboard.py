from turtle import Turtle
ALIGN = 'center'
FONT = ('Gongster', 24, 'bold')

class Scoreboard(Turtle):
    
    def __init__(self, height):
        super().__init__()
        self.height = height
        self.left_score = 0
        self.right_score = 0
        self.pu()
        self.hideturtle()
        self.color('#ffffff')
        self.teleport(0 , self.height/2 - 40)
        self.write(f'{self.left_score} : {self.right_score}', False, ALIGN, FONT)
        
    def updateScore(self, pos):
        if pos == 'right':
            self.left_score += 1
            self.clear()
            self.write(f'{self.left_score} : {self.right_score}', False, ALIGN, FONT)
        else:
            self.right_score += 1
            self.clear()
            self.write(f'{self.left_score} : {self.right_score}', False, ALIGN, FONT)
    
    def gameStatus(self):
        if self.left_score == 12 or self.right_score == 12:
            self.teleport(0,0)
            self.write('GAME OVER', False, ALIGN, FONT)
            return False
        else:
            return True