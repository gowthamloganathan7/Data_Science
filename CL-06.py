# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:45:55 2023

@author: Gowtham
"""

############### """" FOR LOOP """" ##################################

for i in range(0,10):
    print(i)
    
name = ["aaa","bbb","ccc","ddd","eee","fff"]

for i in name:
    print(i)
    
for i in "gowtham":
    print(i)


for i in range(0,10,3):
    print(i)
'''
output
0
3
6
9
'''
for i in name:
    print(i)
    if i=="ccc": #it will stop when "ccc" is printed
        break
'''output
output:
aaa
bbb
ccc
'''
for i in name:
    if i=="ccc": #it will skip the "ccc" from the output
        continue
    print(i) 
'''output
output
aaa
bbb
ddd
eee
fff
'''

name=["aaa","bbb","ccc","ddd","eee","fff"]
i=-1
while i<len(name)-1:
    i=i+1
    if name[i]=="ccc": #it will skip ccc and print remaining values
        continue
    print(name[i])
'''output
output
aaa
bbb
ddd
eee
fff
'''

emp={23:"nlg",55:"muk",66:"rah"}

for i in emp.keys(): #it will print the key in dict
    print(i)
'''output
output
23
55
66
'''
for i in emp.values():#it will print the values in dict
    print(i)
''' output
output
nlg
muk
rah
'''
for i in emp.items():
    print(i)
'''
output
(23, 'nlg')
(55, 'muk')
(66, 'rah')
'''
for i, j in emp.items():
    print("i",i,"j",j)
'''output
i 23 j nlg
i 55 j muk
i 66 j rah
'''


####################### """" function """"" ################################

#user defined func
#inbuild function

#func call
#func def

def func():  #define the functon
    print("hi")

func() #calling the fuction

def func1(x,y):
    x=x+3
    y=y+3
    print("values add with '3'", x, y)
func1(20,30) # values given inside the () is called arguments
'''output
values add with '3' 23 33
'''
x = -100
y = 90
def func2(x,y):
    print(x-y)
    
func2(y,x) # func2(90-(-100))=90+100=190

def func3(x,y):
    x=x+20
    print("x",x)
    print("y",y)
    
x=20
y=30
func3(x,y)
''' output
x 40
y 30
'''

#function using return
def func4(x,y):
    z=x**2+y**2 
    return z
x = 10
y = 20 
a = func4(x,y)
print(a) #out 500


################# creating tables using for loop ##########################
a = 2
for i in range(1,11):
    print(i ,"x",a,"=", i*a)
'''
output
1 x 2 = 2
2 x 2 = 4
3 x 2 = 6
4 x 2 = 8
5 x 2 = 10
6 x 2 = 12
7 x 2 = 14
8 x 2 = 16
9 x 2 = 18
10 x 2 = 20
'''

