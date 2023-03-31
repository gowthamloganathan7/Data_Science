# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:52:33 2023

@author: Gowtham
"""


class emp:
    def __init__(aaa,id,name,age):
        aaa.id = id
        aaa.name = name
        aaa.age = age
    def dis(a):
        print("hi",a.id, "name:",a.name, "\nage:" ,a.age)
    def mod(a1,new_name):
        a1.name = new_name
    
e1 =emp(26,"nlg1",28)

print(e1.dis())

e1.mod("gow")

e1.dis()