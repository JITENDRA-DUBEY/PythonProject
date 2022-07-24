import turtle
import pandas
from turtle import Turtle,Screen
screen = Screen()
screen.title("U.S State Games")

#screen.bgpic("blank_states_img.gif")


image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_state=[]

while len(guessed_state)<50:
    answer_state = screen.textinput(title=f"Guess The State {len(guessed_state)}/50",
                                    prompt="what is an another state name ? ").title()
    if answer_state=="Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
                df = pandas.DataFrame(missing_state)
                df.to_csv("Learned_state.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state==answer_state]# it return data frame
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        #t.write(state_data.state.item())
# herewe generse a state csv which is not guessed by user

