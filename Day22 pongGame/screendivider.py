from turtle import Turtle
class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0,-300)
        self.setheading(90)
        self.pensize(8)
        self.move()



    def move(self):
        game_is_on=True
        while game_is_on:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            if self.ycor()>280:
                game_is_on=False

