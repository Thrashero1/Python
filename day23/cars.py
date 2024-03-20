from turtle import Turtle
import random
colours = ['#130d34', '#a3eef5', '#1a0a23', '#0ff2a4', '#1b2def', '#03423a']
START_SPEED = 5
SPEED_INCR = 5


class Cars():
    
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.allcars = []
        self.speed = START_SPEED
        self.car_amount = 15
        
    
    def createCar(self):
        rand_create = random.randint(1, self.car_amount)
        if rand_create == 1 or rand_create == 2:
            newCar = Turtle('square')
            newCar.pu()
            newCar.shapesize(1,2,1)
            rand = random.randint(0, len(colours)-1)
            newCar.color(colours[rand])
            rand_y = random.randint(int(-(self.height/2) + 60), int(self.height/ 2 - 60))
            newCar.teleport(self.width/2 + 20, rand_y)
            self.allcars.append(newCar)
            
    def moveCars(self):
        for car in self.allcars:
            car.backward(self.speed)
            # new_x = car.xcor() - START_SPEED
            # car.goto(new_x, car.ycor())
    
    def increaseSpeed(self):
        self.speed += SPEED_INCR
        if self.car_amount > 4:
            self.car_amount -= 1
    
    def checkCollision(self, frog):
        for car in self.allcars:
            if car.distance(frog) < 20 and frog.ycor() <= car.ycor() + 20 and frog.ycor() >= car.ycor() -20:
                return False
            else:
                return True