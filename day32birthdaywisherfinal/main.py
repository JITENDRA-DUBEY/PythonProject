# 1. Update the birthdays.csv with your friends & family's details.
import datetime as dt
import pandas
import random
import smtplib

# HINT: Make sure one of the entries matches today's date for testing purposes.
today=dt.datetime.now()
today_tuple=(today.month,today.day)
# 2. Check if today matches a birthday in the birthdays.csv
data =pandas.read_csv("birthdaydat.csv")

# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
birthday_dict={(data_row.month,data_row.day): data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person=birthday_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # 587 port address
        connection.starttls()
        connection.login(user="senderemail192@gmail.com", password="oupsrazomfmwvsiv")
        connection.sendmail(from_addr="senderemail192@gmail.com", to_addrs=birthday_person["email"],
                            msg=f"Subject:Birthday Wish\n\n{contents}")

    print("jd")
# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

