#jsg
import turtle
from turtle import Turtle
import random
turtle.colormode(255)
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color(self.random_colorfood())#there may be problem when there is black color food it not show on screen
        self.speed("fastest")
        self.penup()
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)
    def random_colorfood(self):
        r=random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        my_color=(r,g,b)
        return my_color






















# X=200
# Y=200
# #creating an random food
# tim = Turtle()
# tim.hideturtle()
# tim.penup()
# for i in range(20):
#     tim.setpos(random.randint(-200,X),random.randint(-200,Y))
#     tim.dot(20,"black")

#screen=Screen()
#screen.exitonclick()