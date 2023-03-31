
a = "google_pixel_6"

a[2]

a[2:9]

a[:9] #it will start from the 0 and ends at 8

a[2:] #it will start from 2 and ends at infinity

a[2:1000] #it will starts from 2 and ends at 999

a[::-1] #it will print in reveres order

""" ALWAYS STARING VALUE SHOULD BE LESSER THEN ENDING VALUE """

a[3:3] #no value

a[8:3] # no value

a[0:14:1] 

a[0:14:3] # it will print multiple of 3 

a[14:0:-2]

a[-14:-3]

a[-14:5]

dir(str)

name =input("give name:")
location = input("you location:")
salary = input("your salary")

print("hi my name",name,"and i'm coming from",location, "my salary is",salary)
print("hi my name "+name+" and i'm coming from "+location +" my salary is "+str(salary)) #concadination method

s =("hi my name {} and i'm coming from {} my salary is {}")
s.format(name,location,salary)

s.format("sindhu","TJ","3000")

a=["karthi","sbc","4000"]

s.format([a])

import time

x =time.ctime()
print(x)

import datetime
import pytz

ist = pytz.timezone("asia/kolkata")

time =datetime.datetime.month(ist)
print(time)

dir(pytz)
dir(datetime.datetime.time)


################    Task #################################

import datetime

total_amount =10000
name =input("please enter your name: ")
amount = int(input("enter amount: "))
bank_name = input("enter your bank name: ")
balance_amount =(total_amount-amount)

date = datetime.datetime.now()

statement = ("hi {} you withdrawn {} from {} bank at {} and your available balance is {}").format(name,amount,bank_name,date,balance_amount)

print(statement)







