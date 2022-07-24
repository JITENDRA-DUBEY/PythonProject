#jsg
from turtle import Turtle
MOVE_DIS=20
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

#in this class we make a move function which move snake forward
class Snake:
    def __init__(self):

        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITION:   #creating a snake object
            new_segment = Turtle("square")
            new_segment.color("white")
            self.segments.append(new_segment)
            new_segment.penup()
            new_segment.goto(position)
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DIS)
    def extend(self):
        # # add a one more segment at the last pos
         new_segm=Turtle("square")
         new_segm.color("white")
         new_segm.penup()
         new_segm_x=self.segments[len(self.segments)-1].xcor()
         new_segm_y = self.segments[len(self.segments)-1].ycor()
         self.segments.append(new_segm)
         #my_pos = (new_segm_x, new_segm_y)
         new_segm.goto(new_segm_x, new_segm_y)
    def tail_collosion(self):
        for position in self.segments:
            if(position!=self.head):
                 if self.head.distance(position)<15:#collisoon occour
                    return True
        return False
    def Up(self):
        if self.head.heading()!=DOWN:#not down
            self.segments[0].setheading(90)
    def Down(self):
        if self.head.heading() != UP:#not up
            self.segments[0].setheading(270)
    def Right(self):
        if self.head.heading() != LEFT:#not left
            self.segments[0].setheading(0)  #segments[0] represents the head of the snake
    def Left(self):
        if self.head.heading() != RIGHT:#not right
            self.segments[0].setheading(180)
    def reset(self):
        for i in range(0,len(self.segments)):
            self.segments[i].goto(1000,1000)
