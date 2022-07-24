# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import json
from tkinter import messagebox # ut is not a class so we cant import it by using *
import pyperclip
import random
image="Data1.json"
def pass_gen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    char_list = [random.choice(letters) for _ in range(2, random.randint(4, 8))]
    #print(char_list)
    num_list = [random.choice(numbers) for _ in range(2, random.randint(3, 7))]
    #print(num_list)
    symbool_list = [random.choice(symbols) for _ in range(2, random.randint(3, 5))]
    #print(symbool_list)
    password_list = char_list + num_list + symbool_list
    random.shuffle(password_list)
    print(password_list)
    password = ""
    # for char in password_list:
    #     password += char
    password="".join(password_list)
    print(password)
    pass_name.delete(0,END)# this is used to remove old content from label
    pass_name.insert(0,password)# to wrte the password into pass_name erntyry box
    messagebox.showinfo(title="Generate Password",message=f"This is Generated Password : {password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():# it take input from email ,id,pass and save data into file when user click add button
    decison=False
    web = web_name.get()
    email = user_name.get()
    passw = pass_name.get()
    #messagebox.showinfo(title="Website", message="webnamms")
    #generate two buttons which gave yes or no
    if(len(web)==0 or len(passw)==0):
        messagebox.showinfo(title="INFO",message="Hey Please fill complete details")
    else:
        decison= messagebox.askokcancel(title="Info",message=f"website name: {web}\nEmail : {email}\npassword : {passw}\n Is it ok or not?")
        if decison==True:
          new_data={
              web : {
              "email":email,
              "password":passw,
          }
          }
          # here exception may be occur when data1 is empty

          try:
              with open(image,"r") as file:
                data = json.load(file)
              #print(f"sdsa{data}")# this is python dictionary
          except FileNotFoundError:
              with open(image, "w") as file:
                  json.dump(new_data, file, indent=4)#when file is not present than create a file and add data on it
              print("except")

          else:# this execute when there is no exception
              data.update(new_data)#update your old data
              with open(image, "w") as file:
                json.dump(data,file,indent=4)# this added new data into dictionary
              #load json file data

          #print(data["Facebook"])
          finally:
            #print(web, email, passw)
            web_name.delete(0,END)
            pass_name.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# jsg
FONT=("Arial",12,"bold")
from tkinter import*
window=Tk()
window.title("My Password Manager")
window.config(padx=50,pady=50)
# create a canvas
canvas = Canvas(width=200,height=200)

# lets add image to canvas
lock_image= PhotoImage(file="logo.png")
# attach with window
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1,row=0)


#here we have to create text label and buttons
# create a website level at (0,1
website_level= Label(text="Website : ",font=FONT)
website_level.grid(column=0,row=1)

# create a text labele
web_name =Entry(width=35,highlightthickness=2,highlightcolor="blue")
web_name.grid(column=1,row=1)
web_name.focus()

#user_name

user_level= Label(text="Email/Username : ",font=FONT)
user_level.grid(column=0,row=2)
user_name =Entry(width=35,highlightthickness=2,highlightcolor="blue")
user_name.grid(column=1,row=2)
user_name.focus()
user_name.insert(END,"jitendradubey@gmail.com")

pass_level= Label(text="Password : ",font=FONT)
pass_level.grid(column=0,row=3)
# for pas
pass_name =Entry(width=21,highlightthickness=2,highlightcolor="black")
pass_name.grid(column=1,row=3,columnspan=1)

# create a generate key
generate_pass=Button(text="Generate Password",font=FONT,command=pass_gen)
generate_pass.grid(column=2,row=3)

# add key
add_pass=Button(text="Add",font=FONT,width=36,command=save_pass)
add_pass.grid(column=1,row=4,columnspan=2)

# add a search button

def search():
        # print("Search button clicked")
        # here u create a popup which has website name and their password
        # here we use website name as a key of dictionary and than show emailid and password
        #messagebox.showinfo(title="Your pass info",message=f"Website :{web_name.get()}\npassword: {pass_name.get()}")
        website_name=web_name.get() # this we use as a key
        try:
          with open(image,"r") as data_file:
            my_data=json.load(data_file)# it returns a dictionary
        except FileNotFoundError:
           messagebox.showinfo(title="Your pass info", message="Data File not found so please cllick on add key It will create file and add data ")
        #print(my_data[website_name])# if key not present than it through keyvalue error exception
        else:
            try:
                my_info_dict=my_data[website_name]# this returns a dictionary

            except KeyError:
                messagebox.showinfo(title="Your pass info",message="This website data is not saved in our record you have to first add data")
            else:
                user_email=my_info_dict["email"]
                user_pass=my_info_dict["password"]
                messagebox.showinfo(title="Your pass info",message=f"Email:{user_email}\npassword={user_pass}")

search_button= Button(text="Search",font=FONT,command=search,width=10)
search_button.grid(column=2,row=1)

window.mainloop()