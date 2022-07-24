#jsg
from turtle import Turtle,Screen
import random
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_positions=[(0,0),(-20,0),(-40,0)]
segments=[]
for position in starting_positions:
    new_segment=Turtle("square")
    new_segment.color("white")
    segments.append(new_segment)
    new_segment.penup()
    new_segment.goto(position)
# our task is to move whole segment by on

game_is_on=True
# while game_is_on:
#     screen.update()#only update the screen when whole segment move forward
#     time.sleep(0.1)
#     for seg in segments:
#         #screen.update()
#         seg.forward(20)
#         #time.sleep(0.1)
## hoe to turn left
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1,0,-1):
        new_x=segments[seg_num-1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)
    #segments[0].left(90)
# def turn_left():
#     screen.update()
#     time.sleep(1)
#     segments[0].left(90)
#
#     segments[0].forward(20)
#
#     segments[1].forward(20)
#
#     segments[2].forward(20)
#     screen.update()
#
# turn_left()





screen.exitonclick()