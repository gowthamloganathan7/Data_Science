# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:26:51 2023

@author: Gowtham
"""
'''
################## """"Dictionary""""""""  ###########################

#change, unordered, in values duplicates allowed, key duplicates not allowed 

emp = {45: "nlg", 55: "muk", 33: "rah"}

emp[45] #it will print the key 45 value

emp[55]= "mukunth" # it will replace the value
emp

emp[35] ="nir" #if the key was not there new key value will be create inside the dict
emp

dir(dict)

#keys
emp.keys() #shows the key present in the dict
#values
emp.values() #shows the value present the dict
#update
emp.update({77:"anu"})
emp

emp.update({45:"nlg1"})
emp
#popitems
emp.popitem() #last value will be deleted and no arguments will not will provide inside the ()
emp
#pop
emp.pop(45) #need to provide argument inside the ()
emp

emp["emp_id"]={25,30,40} #we can add anything inside the dict by giving key value
emp


######################### """"" SET """""" ###################################

#unorder, can't update, can add and remove
#it will automatically sort the value inside the {} like numerical, uppercase, lowercase

a = {"aaa", "bbbb","cccc","dddd","eeee"}
a,type(a)

a = {"aaa","aaa","aaa","bbb","ccc"} 
a                                   #so it removed the duplicate value

a = {"aaa","BBB","cccc","DDD",23,1,"ccc",0.5}
a                                   #so it sort the values by numerical, uppercase, lowercase

#add
a.add("ddd")
a
#remove
a.remove("ccc")
a
#a.remove("aaaa") #if there is no value like this it will note remove it 
#a

#difference:-
b={"aaa","bbb","ccc","ddd"}
b1 ={"eee","fff","aaa"}

b2 = b.difference(b1) #it will subtract the value b - b1 and shows the remaining value inside the b 
b2

#symmetric_difference:-
result = b.symmetric_difference(b1) #it add both the variable and remove the same values present the variable
result

#difference_update:-
b.difference_update(b1) #b =b-b1 it will subtract the b and b1 and value will be assigned to b
b

#pop:-
result.pop() #it will remove the data randomly
print(result)

result.pop()
result

#Intersection:-
r = b.intersection(b1) #it will show the comman values in two variable
r

#Subset
name1 ={"aaa","bbb","ccc","ddd"}
name2 ={"eee","fff","aaa"}
name3 ={"ccc","ddd"}

name3.issubset(name1) #so it will check whether all the values name3 present in the name1

name2.issubset(name1) #false

name1.issubset(name3) #false

#Superset
name1 ={"aaa","bbb","ccc","ddd"}
name2 ={"eee","fff","aaa"}
name3 ={"ccc","ddd"}
name4 ={"fff","ccc"}

name1.issuperset(name4)#false
name1.issuperset(name3)#true because all the values in name3 is present inside name1
name1.issuperset(name2)#false
name1.issuperset(name1)#true                     
name2.issuperset(name1)#false
name2.issuperset(name3)#false
name2.issuperset(name4)#false

#Disjoint:-
name1 ={"aaa","bbb","ccc","ddd"}
name2 ={"eee","fff","aaa"}
name3 ={"ccc","ddd"}
name4 ={"fff","eee"}

name1.isdisjoint(name4) #true because there is no relationship between name 1 and name4
name1.isdisjoint(name2) #False because "aaa" is comman in both the variable


################# """Conditional Statement""" ###############################

# ==, < , > , <= ,>=
#if,elif,else:
#if any one condition is true it will print the value

# """"" lets find which number is greater

n1 = int(input("enter value: "))
n2 = int(input("enter value: "))

if n1>n2:
    print("n1 is greater")
elif n1==n2:
    print("N1 & N2 are equal")
else:
    print("n2 is greater")
    
# """"" to find incentive for gender based on the exp

exp = int(input("enter exp: "))
gender = input("ender your gender: ")
incentive = 0

if exp<=5:
    if gender == "male":
        incentive = 4000
    elif gender == "female":
        incentive = 5000
    else:
        incentive =6000
else:
    if gender == "male":
        incentive = 8000
    elif gender == "female":
        incentive = 9000
    else:
        incentive =10000    
print("your exp is",exp,"and your gender is",gender,"based on this your incentive is",incentive)
'''


######################"""""""TASK"""""""""""################################
a= 13
b = 12
c = 11
d = 16
e = 20

if a>b:
    if a>c:
        print("A is greater then C")
    elif a>d:
        print("A is greater then B")
    elif a>e:
        print("A is greater then E")
    else:
        
        if b>c:
            print("A is greater then B")
elif b>c:
    print("B is greater then C")
    if b>d:
        print("b is greater then D")
    else:
        print("bb")
        










