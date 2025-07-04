
import datetime

name = input("Hi there! What's your name? ")
dob = input("Date of birth (DD-MM): ")

today = datetime.datetime.now()
today_str = today.strftime("%d-%m")

if dob == today_str:
    print("🎉 Happy Birthday! !😋😋😋")
else:
    print("🎈 Belated or Advance wishes!😋😝😝")

print("Wishes by Sri Vidhya 💖")