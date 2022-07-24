from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level=0
        self.hideturtle()
        self.writefun()
    def writefun(self):
        self.goto(-280,270)
        self.write(f"Level :{self.level}",font=("Courier", 18, "normal"))
    def inr_score(self):
        self.level+=1
        self.clear()
        self.writefun()
    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER ",align="center", font=FONT)

