#jsg
import requests
import datetime
import smtplib
import time

MY_LATITUDE = 20.9206#this is your current location position
MY_LONGITUDE =-24.3091
# lets take out current position of iss
def iss_overhead():
    response =requests.get("http://api.open-notify.org/iss-now.json")#for stablishing connections
    response.raise_for_status()# for raising exceptions
    data=response.json()#converting into jsondata format
    #print(data)
    Longitude = float(data["iss_position"]["longitude"])
    Latitude =  float(data["iss_position"]["latitude"])
    #iss_pos = (Longitude,Latitude)# current position of iss
    #print(iss_pos)
    if MY_LATITUDE - 5<= Latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= Longitude <= MY_LONGITUDE + 5:
      return True

# current position of your location

def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng":MY_LONGITUDE,
        "formatted":0
    }

    curr_response = requests.get(url="https://api.sunrise-sunset.org/json",verify=False,params=parameters)
    curr_response.raise_for_status()
    data=curr_response.json()
    print(data)
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise,sunset)

    # for current time hour
    curr_time=int(datetime.datetime.now().hour)
    print(curr_time)
    # IF iss current location is nearest to my country location and if it is night than we send mail
    if curr_time>=sunset or curr_time<= sunrise:#that it is night
         return True#it s night
while True:
    if is_night() and iss_overhead():
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user="senderemail192@gmail.com",password="oupsrazomfmwvsiv")
            connection.sendmail(from_addr="senderemail192@gmail.com",to_addrs="jitendradubeybas@gmail.com",msg="Subject:LookUP ISS\n\n You can see ISS on the sky")
        print("sendmail")
    else:
        print("no mail send")
    time.sleep(10)#after each 10 second this loop run



