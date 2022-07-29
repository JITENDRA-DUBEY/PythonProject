BACKGROUND_COLOR = "#B1DDC6"
FONT=("Arial",40,"bold")
#jsg
from tkinter import*
import pandas
import random
import time
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR,padx=20,pady=20)
ftoenglish=""

count=0
# lets create a canvas
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR)
card_front_img=PhotoImage(file="images\card_front.png")
front_image=canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(380,160,text="Title",font=FONT,fill="black")
current_word=canvas.create_text(400,263,text="Actual Word",font=FONT,fill="black")
canvas.grid(column=0,row=0,columnspan=2)# so that here image should be in column 0 to 2
card_back_img = PhotoImage(file="images\card_back.png")

#task2 always generate randow frnech word if use click x \/ key
data=pandas.read_csv("data/french_words.csv")#it return a 2d data frame
#french_word_list=data["French"].to_list()#this is series data frame french_word_list=data["French"]
#print(french_word_list)
my_data_dict=data.to_dict(orient="records")#vvvmithis convert data frame into list of dictionary having french and english as a key
def gen_french_word():
    global fliptimer,count
    window.after_cancel(fliptimer)#here cancel gen french word timer
    canvas.itemconfig(front_image, image=card_front_img)
    french_word_dic=random.choice(my_data_dict)#random.choice(my_data_dict) this generates random dictionaries from that we take french key value
    french_word=french_word_dic["French"]
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(current_word,text=f"{french_word}",fill="black")
    global ftoenglish
    ftoenglish = french_word_dic["English"]
    #here we want to add some functioality so that if we dont call generate function until 3 ec than it call task
    fliptimer=window.after(2000, task)#assign new fliptimer

cross_image = PhotoImage(file="images\wrong.png")
cross_button=Button(image=cross_image,highlightthickness=0,command=gen_french_word)
cross_button.grid(column=0,row=1)

tick_image = PhotoImage(file="images\\right.png")
tick_button=Button(image=tick_image,highlightthickness=0,command=gen_french_word)
tick_button.grid(column=1,row=1)
#task3

def task():#flipcard
    global fliptimer
    canvas.itemconfig(front_image,image=card_back_img)
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(current_word, text=ftoenglish,fill="white")
    window.after(2000, gen_french_word)#after giving english meaning geneate french word


fliptimer=window.after(2000, gen_french_word)# here we call gen french word in every 2 second it there is no intrepution that means if user dont't generate frenech word
gen_french_word()


window.mainloop()



