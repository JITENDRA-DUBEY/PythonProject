from tkinter import *
import requests
window=Tk()
window.title("My KanyoQuote Generator")
window.config(padx=50,pady=50)
def to_get():
    #in this function we get a random quote from api and than write in my text
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()#for exception
    response_quote = response.json()["quote"]# getting qutote from json (like dict
    print(response_quote)
    canvas.itemconfig(my_text,text=response_quote)

my_image = PhotoImage(file="background.png")

canvas = Canvas(width=300,height=414)
canvas.create_image(150,207,image=my_image)
my_text=canvas.create_text(150,207,text="Kanye Quote start here ",font=("Arial",24,"bold"),width=250)
canvas.grid(column=0,row=0)
# lets creatae an image button with emoji
kanye_img=PhotoImage(file="Kanye.png")
button = Button(image=kanye_img,command=to_get)
button.grid(column=0,row=1)
window.mainloop()
print("Jd")