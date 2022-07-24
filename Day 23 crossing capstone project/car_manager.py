from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_move_dis = [5]
MOVE_INCREMENT = 2
All_Cars=[]
class CarManager(Turtle):
    def __init__(self):
      super().__init__()
      self.shape("square")
      self.shapesize(stretch_wid=1,stretch_len=2)
      self.color(random.choice(COLORS))
      self.penup()
      self.goto(320,random.randint(-250,250))
      All_Cars.append(self)
    def move_car(self):
        #move a random car from append list
        for car in All_Cars:
          car.backward(starting_move_dis[len(starting_move_dis)-1])
    def new_cargen(self):
        random_num=random.randint(1,6)
        if random_num==1:
            return True # when 1 get than genearate new car
    def inr_speed(self):
        starting_move_dis.append(starting_move_dis[len(starting_move_dis)-1]+MOVE_INCREMENT)