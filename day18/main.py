from turtle import *
import random
# import colorgram as cg

tim = Turtle()
screen = Screen()

# colours = cg.extract('hirst.jpg', 30)
my_colours = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     color_tuple = (r, g, b)
#     my_colours.append(color_tuple)

# angles = [90, 180, 270, 0]

# tim.shape('turtle')
tim.hideturtle()
screen.colormode(255)
tim.pensize(1)
tim.speed(0)
y_pos = -200
x_pos = -200
movement = 50


tim.pu()

tim.pd()
def tim_move_to(x, y):
    tim.pu()
    tim.setpos(x, y)
    tim.pd()
    


for x in range(10):
    tim_move_to(x_pos, y_pos)
    for y in range(10):
        tim.dot(20, random.choice(my_colours))
        tim.pu()
        tim.fd(50)
        tim.pd()
    y_pos += movement
    


# def dashed_line():
#     for x in range(10):
#         tim.fd(10)
#         tim.pu()
#         tim.fd(10)
#         tim.pd()
        
# def shapes(sides):
#     angle = 360 / sides
#     for x in range (sides):
#         tim.fd(100)
#         tim.rt(angle)

# sides = 3

# while sides <= 10:
#     r = int(random.randint(1, 255))
#     g = int(random.randint(1, 255))
#     b = int(random.randint(1, 255))
#     tim.color(r, g, b)
#     shapes(sides)
#     sides += 1

      
# for x in range (4):
#     dashed_line()
#     tim.rt(90)
# for x in range(1000):
#     r = int(random.randint(0, 255))
#     g = int(random.randint(0, 255))
#     b = int(random.randint(0, 255))
#     tim.color(r, g, b)
#     tim.fd(50)
#     tim.setheading(random.choice(angles))
# def spirograph(move):
#     angle = 0
#     while angle <= 360:
#         r = int(random.randint(0, 255))
#         g = int(random.randint(0, 255))
#         b = int(random.randint(0, 255))
#         tim.color(r, g, b)
#         tim.circle(100)
#         angle += move
#         tim.setheading(angle)
# spirograph(5)  

screen.exitonclick()