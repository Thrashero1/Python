from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    
    
    def __init__(self, segments) -> None:
        self.snakes = []
        self.createSnake(segments)
        self.head = self.snakes[0]
    
    def createSnake(self, segments):
        start_x = 0
        for x in range (0, segments):
            self.add_seg(start_x, 0)
            start_x -= 10
    
    def add_seg(self, start_x, start_y):
        snake = Turtle('square')
        snake.shapesize(0.5,0.5)
        snake.color('#ffffff')
        snake.teleport(start_x, start_y)
        snake.pu()
        self.snakes.append(snake)
        
    def move(self):
        for s in range(len(self.snakes)- 1, 0, -1):
            x = self.snakes[s-1].xcor()
            y = self.snakes[s-1].ycor()
            self.snakes[s].goto(x, y)
        self.head.fd(10)
        
    def checkEdge(self, height, width):
        if int(self.head.xcor()) >= (width / 2):
            print('You have hit a wall')
            return False
        elif int(self.head.xcor()) <= -(width / 2):
            print('You have hit a wall')
            return False
        elif int(self.head.ycor()) >= (height / 2):
            print('You have hit a wall')
            return False
        elif int(self.head.ycor()) <= -(height / 2):
            print('You have hit a wall')
            return False
        else:
            return True
        
    def goUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def goLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def goDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def goRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def increasesize(self):
        x_pos = self.snakes[-1].xcor()
        y_pos = self.snakes[-1].ycor()
        self.add_seg(x_pos, y_pos)
    
    
    
    
        