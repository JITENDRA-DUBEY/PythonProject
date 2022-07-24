
import turtle
from turtle import Turtle, Screen
from paddleclass import Paddle
from ballclass import Ball
from scoreboard import Score
from screendivider import Divider
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
divider = Divider()
screen.tracer(0)
r_paddle=Paddle(380,0)
l_paddle=Paddle(-390,0)


ball=Ball()
score=Score()




screen.listen()
screen.onkey(key="Up",fun=r_paddle.up)
screen.onkey(key="Down",fun=r_paddle.down)
#for controlling left paddle we use w for up sfor down
screen.onkey(key="w",fun=l_paddle.up)
screen.onkey(key="s",fun=l_paddle.down)
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    #detect the collisoon with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        #call boiunce function
        ball.bounce_y()
    #detect the collisoon of ball with the paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>325 or ball.distance(l_paddle)<50 and ball.xcor()<-325:
        ball.bounce_x()
        ball.incr_speed()
    #detect the ball miss by r_paddle and restart the ball from origion and move towards to ither player
    if ball.xcor()>380:
        #ball.hideturtle()
        #ball=Ball()
        #ball.showturtle()
        ball.reset_pos()
        ball.bounce_x()
        score.inrl_score()
        #maintain its original speed
        ball.original_speed()
        #when rpaddle missed than increase scroe of lpaddle

    if ball.xcor()<-380:
        ball.reset_pos()
        ball.bounce_x()
        score.inrr_score()
        ball.original_speed()


screen.exitonclick()