STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    def move(self):
        self.forward(MOVE_DISTANCE)
    def Up(self):
        self.move()
    def left(self):
        #move to x axis po
       new_x=self.xcor()-MOVE_DISTANCE
       self.goto(new_x,self.ycor())
    def right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())
    def reset_pos(self):
        # if it turtle collide with upper wall than it restart from starting pos
        if self.ycor()>FINISH_LINE_Y:
          self.goto(STARTING_POSITION)
          return True# fo increasing turtle speed
        return False
