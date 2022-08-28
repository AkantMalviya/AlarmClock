import datetime as dt
from playsound import playsound

playsound("beep.mp3")
print("\t<Alarm Clock>")
print("\n SET THE ALARM")
alarmhour = int(input("Enter Hour : "))
alarmmin = int(input("Enter Minute : "))
alarmpm = input("AM or PM : ").lower()

if alarmpm == "pm":
    alarmhour += 12

while True:
    if alarmhour == dt.datetime.now().hour and alarmmin == dt.datetime.now().minute:
        print("Alarm is ringing")
        playsound("beep.mp3")
        break
