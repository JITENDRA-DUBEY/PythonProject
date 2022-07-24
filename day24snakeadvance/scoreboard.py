#jsg
import time
from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 22, "normal")
high_score=[0]
#here we maintain high_score from file
#at initial in while we self put 0 as a high score
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score=0
        self.highscore=0
        #self.highscore=0
        self.penup()
        self.goto(-230,270)
        self.write(f"Score : {self.score}", True, align="left",font=FONT)
        self.goto(80,270)
        with open("high_scorefile.txt") as file:
            my_high_score=file.read()
        self.write(f"HighScore : {my_high_score}", True, align="left", font=FONT)

    def increase_score(self):
        self.score+=1
        self.goto(-230, 270)
        self.clear()
        self.write(f"Score : {self.score}", True, align="left", font=FONT)
        self.goto(80, 270)
        with open("high_scorefile.txt") as file:
            my_high_score = file.read()
        self.write(f"HighScore : {my_high_score}", True, align="left", font=FONT)
        #self.high_score()

    def game_over(self):
        with open("high_scorefile.txt") as file:
            sc=file.read()
        if str(self.score)>sc:
            #high_score.append(self.score)
            with open("high_scorefile.txt",mode="w") as file:
                file.write(str(self.score))

        self.score=0
        self.clear()
        self.goto(-230, 270)
        self.write(f"Score : {self.score}", True, align="left", font=FONT)
        self.goto(80, 270)
        with open("high_scorefile.txt") as file:
         my_high_score = file.read()
        self.write(f"HighScore : {my_high_score}", True, align="left", font=FONT)
        #self.write(f"High Score : {high_score[len(high_score)-1]}", True, align="left", font=FONT)
        self.goto(-80,0)
        self.write("GAME OVER",font=FONT)
        time.sleep(0.2)
        self.clear()
        self.goto(-230, 270)
        self.write(f"Score : {self.score}", True, align="left", font=FONT)
        self.goto(80, 270)
        with open("high_scorefile.txt") as file:
            my_high_score = file.read()
        self.write(f"HighScore : {my_high_score}", True, align="left", font=FONT)



