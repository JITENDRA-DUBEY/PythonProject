
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT=(FONT_NAME,"18","bold")
res=0
timer=None
#mark=""

#jsg
from tkinter import*

# ---------------------------- TIMER RESET ------------------------------- # 
def start_used():
        global res
        res+=1
        if res%8==0:
            count_down(60 * LONG_BREAK_MIN)
            timer_level.config(text="Break", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)

        elif res%2==1:
            count_down(60 * WORK_MIN)
            timer_level.config(text="Work", font=(FONT_NAME, 50), fg=PINK, bg=YELLOW)
            # global mark
            # mark += "✔"
            # check_button.config(text=mark)# as work complete

        else:
            count_down(60 * SHORT_BREAK_MIN)
            timer_level.config(text="S Break", font=(FONT_NAME, 50), fg=RED, bg=YELLOW)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def restart_used(): # strat timer from from starting res=1;erase all ticks , change lebel to timer
    #
    # #res=1
    # count_stop=1
    #
    window.after_cancel(timer)
    timer_level.config(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    check_button.config(text="")
    global res
    res=0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
import math
#time.sleep()
def count_down(count):
    global timer
    global res
    count_sec=count%60
    count_min=math.floor(count/60)
    if count_min < 10:
        count_min = str("0" + str(count_min))
    if count_sec<10:
        count_sec=str("0"+str(count_sec))
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if(count>0):
        print(count)
        timer= window.after(1000,count_down,count-1)

    else:
        start_used()# again triggring start
        mark=""
        complete_session=math.floor(res/2)#work break 5 min
        for _ in range(complete_session):
            mark += "✔"
        check_button.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW )

#window.minsize(width=600,height=600)
canvas=Canvas(window,width=200,height=224,bg=YELLOW,highlightthickness=0)#equal to image size
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img,anchor="center")
# lets write on tomato image
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,20,"bold"))
canvas.grid(column=1,row=1)
#count_down(5)

# lets add timer level at up
timer_level=Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
timer_level.grid(column=1,row=0)

# lets create a start button on the left
start_button=Button(text="Start",font=FONT,command=start_used,width=5,highlightthickness=0)
start_button.grid(column=0,row=2)

#lets create restart button
reset_button=Button(text="Reset",font=FONT,command=restart_used,width=5,highlightthickness=0)
reset_button.grid(column=2,row=2)

#def check button
def check_button():
    print(check_state.get())
check_state=IntVar()
check_button=Checkbutton(text= "",variable=check_state,command=check_button,fg=GREEN,font=FONT,bg=YELLOW)#ones worlk compl
check_button.grid(column=1,row=2)


window.mainloop()

