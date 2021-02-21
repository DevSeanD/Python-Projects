"""
Author: Sean Dever
Description: Currently serving as a foundational calendar logic for a gui to be implemented later on.
Date: 2-21-2021
"""
from datetime import date
dateToday = date.today()

dateToday = str(dateToday)

yearNow = str(dateToday[0]) + str(dateToday[1]) + str(dateToday[2]) + str(dateToday[3])
monthNow = str(dateToday[5]) + str(dateToday[6])
dayNow = str(dateToday[8]) + str(dateToday[9])

print(monthNow,dayNow,yearNow)


class day:
  def __init__(self,month,day,year,data):
    self.m = month
    self.d = day
    self.y = year
    self.d = data

day1 = day(monthNow,dayNow,yearNow,"This is a test of the data attribute")

feb = []
for d in range(1,29):
  feb.append(d)

showFeb = feb
counter = 0
for elm in range(0,len(feb)):
  if(counter == 5):
    print()
    counter = 0
  print(showFeb[elm],end="\t")
  counter += 1
print()

for d in range(0,len(feb)):
  feb[d] = day(monthNow,d,yearNow,"Test")

print("Options")
print("#######")
print("1 - Add Event")
opt = input("")

if opt == '1':
   dayIn = input("Enter the day of the month you would like to add an event to: ")
   dataIn = str(input("What time is the event: "))
   dataIn += " - "
   dataIn += str(input("Describe the event: "))
   feb[int(dayIn)].d = dataIn
   print(feb[int(dayIn)].d)
  
