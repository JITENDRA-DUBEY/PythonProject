##################### Birthday Wisher ######################
#jsg

import pandas
import datetime as dt
import random
import smtplib
now=dt.datetime.now()
today_day=now.day
today_month=now.month
today_year=now.year


data= pandas.read_csv("birthdaydat.csv")

my_data_dict=data[data.day==today_day].to_dict()#it return a dataframe row of today day so we convert ths data frame into dict
#print(my_data_dict)
#here my task is know the index of row
index_of_row=list(my_data_dict["name"].keys())[0]# it return first key


if my_data_dict["month"][index_of_row]==today_month :
    #that means today is birthday we randomly select a templates from letter and send happy birthday
    num= random.randint(1,3)
    my_file="letter_"+str(num)+".txt"
    print(my_file)
    with open(f"letter_templates/{my_file}") as file:
       my_file_data=file.read()
    my_file_data= my_file_data.replace("[NAME]",my_data_dict["name"][index_of_row])# here we change our text
    #3sendemail
    with smtplib.SMTP ("smtp.gmail.com",587) as connection:#587 port address
        connection.starttls()
        connection.login(user="senderemail192@gmail.com",password="oupsrazomfmwvsiv")
        connection.sendmail(from_addr="senderemail192@gmail.com",to_addrs=my_data_dict["email"][index_of_row],
                            msg=f"Subject:Birthday Wish\n\n{my_file_data}")

print("jd")



