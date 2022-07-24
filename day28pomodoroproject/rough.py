#jsg
from tkinter import*
window =  Tk()
window.title("My jd")


# def say_something(a,b,c):
#     print(a,b,c)
#
# window.after(1,say_something,2,3,4)
def count_down(count):
    print(count)
    if count>0:
     window.after(1000,count_down,count-1)# it is like recuursion each time function calll itelf by passing org-1
count_down(5)
print("jd")
window.mainloop()
