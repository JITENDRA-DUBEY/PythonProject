import turtle
from turtle import Turtle, Screen
#jsg
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(x, y)
    def up(self):
        xpos = self.xcor()
        ypos = self.ycor()+20
        self.goto(xpos, ypos)

    def down(self):
        xpos = self.xcor()
        ypos = self.ycor() - 20
        self.goto(xpos, ypos)



# paddle = Turtle("square")
# #paddle.hideturtle()
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.color("white")
# paddle.penup()
# #paddle.speed("fastest")
#
# paddle.goto(350,0)
# #paddle.showturtle()
# #screen.update()
# def up():
#    #screen.update()
#    #that means only x pos will be changes
#    xpos=paddle.xcor()
#    ypos=paddle.ycor()+20
#    paddle.goto(xpos,ypos)
# def down():
#     #screen.update()
#     xpos = paddle.xcor()
#     ypos = paddle.ycor() - 20
#     paddle.goto(xpos, ypos)
