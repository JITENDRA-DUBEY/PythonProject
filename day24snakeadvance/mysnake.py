import turtle
from turtle import Turtle,Screen
from snakeclass import Snake
from food import Food
from scoreboard import Score
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score= Score()
#highscore=Score()
#highscore.high_score()
screen.listen()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(key="Right", fun=snake.Right)
    screen.onkey(key="Left", fun=snake.Left)
    screen.onkey(key="Up", fun=snake.Up)
    screen.onkey(key="Down", fun=snake.Down)
    cx=snake.head.xcor()
    cy=snake.head.ycor()
    #for boundary collision
    if cx<=-295 or cx>=295 or cy<=-295 or cy>=295: # cllision with walls
        #game_is_on=False
        #food.clear()
        score.game_over()
        #here we have to restart the game that means clear all thing from the screen and create a new snake and new food
       #turtle.clear()
        snake.reset()
        snake=Snake()
        #game_is_on = True
        #here also print the hiogh score
    # next task is to decide the collison with the food if food found than generate a new food and increse a square in snake size
    # than means food x and y cordinate is same as the snake head cordinates
    if snake.head.distance(food)<15:#collison with food is 10*10
       food.hideturtle()
       food = Food()  # new food generate
       score.increase_score()
       snake.extend()
    #for checking tail collision
    if snake.tail_collosion():
        score.game_over()
        #again restart the game
        #turtle.clear()
        snake.reset()
        snake = Snake()
        #game_is_on = False
screen.exitonclick()

