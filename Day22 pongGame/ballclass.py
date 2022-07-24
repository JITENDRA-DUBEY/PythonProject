from turtle import Turtle
import random
#turtle speed list when ball hit paddle than it increase balls speed
#turtle_speed=["slowest","slow","normal","fastest","fast"]

X=380
Y=280
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_ball()
        self.scount = 0
        self.move_speed=0.1

    def move_ball(self):
        #x postion is fix
        #random_pos=(380,random.randint(-280,280))
        new_x=self.xcor()+self.x
        new_y=self.ycor()+self.y
        self.goto(new_x,new_y)
    def bounce_y(self):#change the direction in which ball is move
        self.y*=-1
    def bounce_x(self):#change the direction in which ball is move
        self.x*=-1
    def reset_pos(self):
        self.goto(0,0)

    # when ball hits paddles than increase its speed
    def incr_speed(self):
        self.move_speed*=0.9
     #when paddle miss than restart the ball
    def original_speed(self):
        self.move_speed =0.1



