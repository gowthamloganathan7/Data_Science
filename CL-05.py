'''
# single line condition statement
a= 100
b =200

print("a is greater then b") if a>b else print("b is greater") if b>a else print("equal")
'''
'''
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
'''
# above code as been written in songle line pie
exp = int(input("enter exp: "))
gender = input("ender your gender: ")
incentive = 0

if exp<=5:
    print("incentive= 4000") if gender == "male" else print("incentive = 5000") if gender == "female" else print("incentive = 6000")
else:
    print("incentive= 8000") if gender == "male" else print("incentive= 9000") if gender == "female" else print("incentive=9000")
     
# another way of reducing the line of code
exp = int(input("enter exp: "))
gender = input("ender your gender: ")
incentive = 4000 if exp <= 5 and gender == "male" else 5000 if exp <= 5 and gender == "female" else 6000 if exp <= 5 else 8000 if gender == "male" else 9000 if gender == "female" else 10000
print("your exp is", exp, "and your gender is", gender, "based on this your incentive is", incentive)
'''
'''
###################""""""" LOOP """""""" ###################################

#while loop and for loop

## """""" WHILE LOOP """"""
# 1 init
# 2 cond var
# 3 inc/ dec

# it will print 0 to 9 continously
i = 0
while i<10:
    print(i)
    i=i+1

# it will print multi of 3 upto value present below 20
i = 0
while i<20:
    print(i)
    i=i+3

# it will print division of 3 upto value present below 20
i=0
while i<20:
    if i%4 ==0:
        print(i)
    i=i+1

# find even or odd
i=18
while i<20:
    if i%2 == 0:
        print(i ,"is even number")
    else:
        print(i ,"is odd number")
    break

# find odd or even in single line of code
i=-9
while i<20:
    print(i,"even number") if i%2==0 else print(i , "odd number")
    break

#finding tables using while loop
a= 2
i = 1
while i<=10:
    print(i, "x", a, "=",i*a )
    i=i+1

#printing value inside the list

name= ["aaa","bbb","ccc","ddd","eee","fff"]
i=0
while i<len(name):
    print(name[i])
    i=i+1
name= ["aaa","bbb","ccc","ddd","eee","fff"]

#print it in reverse order
i=0
while i<len(name):
    a= (len(name)-1)-i
    print(name[a])
    i=i+1

#break statement
name= ["aaa","bbb","ccc","ddd","eee","fff"]
i=0
while i<len(name):
    print(name[i])
    if name[i] == "ccc":
        break
    i=i+1

#check whether the given user id and password or correct
user1 ="gowtham"
pass1 ="nlg"
changes = 3
i=1
while i<=3:
    user =input("enter your user id: ")
    password = input("please enter your valid pass: ")
    if user1 == user and pass1 == password:
        print("welcome to python")
        break
    else:
        print("you have entered wrong password and you have ", changes-i, "changes left")
    i=i+1
print("try again later")
'''
a = 5
b = 4
c = 3
d = 20
e = 1

if a>b:
    if a>c:
        if a>d:
            if a>e:
                if a>e:
                    print("a is greater")
                else:
                    print("e is greater")
            elif d>e:
                if a>e:
                    print("d is greater")
                else:
                    print("e is greater")
        elif c>d:
            if c>e:
                if c>e:
                    print("c is grater")
                else:
                    print("e is greater")
            elif d>e:
                if d>e:
                    print("d is greater")
                else:
                    print("e is greater")
elif b>c:
    if b>d:
        if b>e:
            if b>e:
                print("b is greater")
            else:
                print("e is greater")
        elif d>e:
            if d>e:
                print("d is greater")
            else:
                print("e is greater")    
elif c>d:
    if c>e:
        if c>e:
            print("c is greater")
        else:
            print("e is greater")        
else:
    if d>e:
        print("d is greater")
    else:
        print("e is greater")            
 




