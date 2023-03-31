# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:16:47 2023

@author: Gowtham
"""

x =[2,3,4,5,6]
y = x
z = x.copy()
print(y,z)
x.append(100)
print(y,z)

# function with default arguments
def func1(country="India"):
    print("i am from",country)
    
func1("chennai")

def func2(r,pi=3.14): #r=10 pi =3.14, 
    print(pi*r**2) #3.14*10**2. 3.14*100 = 314
func2(10)
'''output
314'''

func2(10,2) #r=10 , pi =2 ; 2*10**2; 2*100 =200
''' output
200 '''

# variable length argument
def func3(*v):
    print(v)
func3(34) # output (34,)

func3(34,21,55,31,23) #output (34, 21, 55, 31, 23)

func3([23,44,22,44])

def func4(*v):
    for i in v:
        print(i)
func4([20,30,40,50])
func4([20,30,40,50],"hi",(20,30,40),20,50) 

def func5(*v):
    for i in v:
        print("data",i,type(i))
func5([20,30,40,50],"hi",(20,30,40),20,50) 
''' output
data [20, 30, 40, 50] <class 'list'>
data hi <class 'str'>
data (20, 30, 40) <class 'tuple'>
data 20 <class 'int'>
data 50 <class 'int'>
'''

# variable length keyword argument:-
# "**var" it will convert into dict

def func6(**v):
    print(v)
func6(n=20,m=30) #output {'n': 20, 'm': 30} <class 'dict'>

func6(n=[20,30,40],m=30,z=(30,50),x={30,40})
''' output
{'n': [20, 30, 40], 'm': 30, 'z': (30, 50), 'x': {40, 30}}
'''

def func7(**v):
    for i,j in v.items():
        print(i,"=",j)
func7(n=[20,30,40],m=30,z=(30,50),x={30,40})
''' output
n = [20, 30, 40]
m = 30
z = (30, 50)
x = {40, 30}
'''
#variable length(*) and variable length keyword(**)
def func8(*a,**b):
    print("a",a)
    print("b",b)
func8("gowtham","nlg",30,n=20,m=50) #it will seperate the first single value goes "a" and values "n=20" will goes to b
''' output
a ('gowtham', 'nlg', 30)
b {'n': 20, 'm': 50}
'''
def func8(*a,**b):
    print("a",a)
    print("b",b)
    
func8("gowtham","nlg",30,n=20,m=50)

def func9(*a,c=None,**b):
    print("a", a)
    print("b", b)
    print("c", c)
func9(40,30,50,"sam",n=10,m=11,c=2)
'''output
a (40, 30, 50, 'sam')
b {'n': 10, 'm': 11}
c 90
'''
def func10(c,*a,**b):
    print("a =",a)
    print("b =",b)
    print("c =",c)

func10(40,30,50,"sam",n=10,m=11)
''' output
a = (30, 50, 'sam')
b = {'n': 10, 'm': 11}
c = 40'''

#multiple return
def func11(a,b,c):
    a1=b+c          #a1=30+40 = 70
    b1=a*c          #b1=20*40 = 800
    c1=a-c          #c1=20-40 = -20
    return a1,b1,c1
    

x= func11(20,30,40)

var = x[0]+x[1]+x[2] #70+800-20 = 850
print(var) #850


x=7
b=(x-1)^3
print(b)



    


    