from turtle import Turtle
ALIGN = 'center'
FONT = ('Gongster', 12, 'normal')



class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.teleport(0, 280)
        self.color('white')
        self.write(f'Score: {self.score}', False, ALIGN, FONT)
        self.hideturtle()
    
    def updateScore(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', False, ALIGN, FONT)
    
    
    def gameOver(self):
        self.teleport(0,0)
        self.write('GAME OVER', False, ALIGN, FONT)