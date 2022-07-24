import time
from turtle import Screen

import car_manager
import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
my_player=Player()
car=CarManager()
score=Scoreboard()
screen.listen()
screen.onkey(key="Up",fun=my_player.Up)
screen.onkey(key="Left",fun=my_player.left)
screen.onkey(key="Right",fun=my_player.right)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #here we have to make car slowy
    if car.new_cargen():
       car=CarManager()
    car.move_car()
    #if player reches to other than we have to increment car movement by 10
    if my_player.reset_pos():  #that it player reaches to other end and comeback to startoing pos
       #now its time to level up
        score.inr_score()
        car.inr_speed()
    #detect turtle collison with car
    for car in car_manager.All_Cars:
        if car.distance(my_player)<20:
            print("Game over")

            score.game_over()
            game_is_on=False




screen.exitonclick()
