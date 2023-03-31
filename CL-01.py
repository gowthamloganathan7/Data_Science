# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:31:35 2023

@author: Gowtham
"""

############### task ####################

amount=int(input("please enter the amount: "))

count1 = amount//2000
remainder1 = amount%2000
print("2000 x",count1, "=", count1*2000)
count2= remainder1//500
remainder2 = remainder1%500
print("500 x",count2, "=", count2*500)
count3= remainder2//200
remainder3 = remainder2%200
print("200 x",count3, "=", count3*200)
count4= remainder3//100
remainder4 = remainder3%100
print("100 x",count4, "=", count4*100)
count5 = remainder4//50
remainder5 = remainder4%50
print("50 x",count5, "=", count5*50)
count6 =remainder5//20
remainder6 = remainder5%20
print("20 x",count6, "=", count6*20)
count7 =remainder6//10
remainder7 =remainder6%10
print("10 x",count7, "=", count7*10)
count8 =remainder7//5 
remainder8 = remainder7%5 
print("5 x",count8, "=", count8*5)
count9 = remainder8//2 
remainder9 = remainder8%2 
print("2 x",count9, "=", count9*2)
count10 = remainder9//1 
remainder10 =remainder9%1 
print("1 x",count10, "=", count10*1)

total1=(count1+count2+count3+count4+count5+count6+count7+count8+count9+count10)
total= ("total number of count:",total1)
print(total)