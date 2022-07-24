#jsg
import turtle
import pandas
from turtle import Turtle,Screen
screen = Screen()
screen.title("U.S State Games")

#screen.bgpic("blank_states_img.gif")


image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
###creqate a score
score=0

tim = Turtle()
tim.hideturtle()
tim.pencolor("black")
data=pandas.read_csv("50_states.csv")#it create a data dataframe(2d)

#here we are going to create a pop screen for answer
game_is_on=True
while game_is_on:
  answer_state=screen.textinput(title=f"Guess The State   {score}/50",prompt="what is an another state name ? ").title()
  #now task is to guessed state is correct or not is yes than write that name on correct position
  check_ans=data[data["state"]==answer_state]#this is dataframe so i  want to create list from that
  if check_ans.empty!=True:# it tells answer is present or not
    my_city=check_ans["state"].to_list()#here we got name as a list
    my_city_name=my_city[0]#take out city  name as a string from my_city list
    x_pos=check_ans["x"].to_list()
    new_x=int(x_pos[0])
    y_pos = check_ans["y"].to_list()
    new_y = int(y_pos[0])
    print(f"{my_city_name} ,. {new_x} ,.{new_y}")
    #here we have to create a turrle and move at x,y pos and also write state name at that place

    tim.penup()
    tim.goto(new_x, new_y)
    tim.pendown()

    tim.write(f"{my_city_name}")
    score+=1
    if score>=50:
      game_is_on=False
      tim.penup()
      tim.goto(-60,0)
      tim.write("You win",font=("Times New Roman", 50, "bold"))


screen.mainloop()#screen is on even mouse clic
#know the coordinates of each staes from 50_states.csv file
# #for x cordintes
# x_cor=data["x"]#it gives series data frame we have to convert in to list
# xcor=x_cor.to_list()
# y_cor=data["y"]#it gives series data frame we have to convert in to list
# ycor=y_cor.to_list()
# city_name=data["state"]
# cityname=city_name.to_list()
# print(cityname)
# print(xcor)
# print(ycor)
# print("jd")
# my_cor=[]
# for i in range(0,len(xcor)):
#     my_tuple=(int(xcor[i]),int(ycor[i]))
#     my_cor.append(my_tuple)
# print(my_cor)
# # lets create a dictionary which have city name and their coordinate




# my_city_data={
#     "city":city_name,
#     "cordiates":my_cor
# }
# print(my_city_data)
# print(type(check_ans))
# print(my_city)
# print(type(my_city))
# print(my_city_name)
# print(type(my_city_name))
# if check_ans["state"]==answer_state:
#   print (check_ans.state)
print("end")