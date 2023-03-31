
###############""""""LAMBDA""""""###################################

#syntex:-
''' lambda arg : exp '''

sample = lambda name : "i am "+name
type(sample) #function
x = sample("gowtham")
''' output
i am gowtham
'''

print("hi guyzz",x)

#using
'''
a=input("enter your name: ")
x = sample(a)
 output
i am gowtham

print("hi guyzz",x)
'''

#(a+b)^2
a_b2= lambda *x: x[0]**2+x[0]**2+(x[0]+x[1])
a_b2(2,2)

a = lambda *x: x[0]+x[1]+x[2]

a([20,50,30],[56,47,69],["nlg","dggf"])
''' output

[20, 50, 30, 56, 47, 69, 'nlg', 'dggf'] '''
# task
a = lambda *x:sum(x)
a(20,30,56,5)

b = lambda *x:sum(x[0])+sum(x[1])+sum(x[2])
b([20,30,50],[60,5,30],[36,45,6])

################# """class and object"""########################

class wwww:
    name="gowtham"
    id = 23

x = wwww() #so x is an object based on wwww
x.name
x.id

y = wwww() #so x is an object based on wwww
y.name
y.id

class emp:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
    location = "chennai"


e1 =emp("gowtham",25,27) 
e1.name,e1.id,e1.age,e1.location 

class emp:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display(self):
        print("hi my id ",self.id,"and my name",self.name,"and my age",self.age)
e1 =emp(25,"gowtham",27)
e1.display()

class emp:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display(self):
        print("hi my id ",self.id,"and my name",self.name,"and my age",self.age)
    def mod(self,new_name):
        self.name = new_name
    def mod_id(self,new_id):
        self.id = new_id
e2=emp(1,"ra",27)
e2.mod("nlg")
e2.display()
e2.mod("nir")
e2.display()
e2.mod_id(6)
e2.display()

class emp: #parent
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display(self):
        print("hi my id ",self.id,"and my name",self.name,"and my age",self.age)
    def mod(self,new_name):
        self.name = new_name
    def mod_id(self,new_id):
        self.id = new_id
class guvi(emp): #child class of emp 
    pass

e3 = guvi(2,"kkk",3)
e3.display()

class emp:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display(self):
        print("hi my id ",self.id,"and my name",self.name,"and my age",self.age)
    def mod(self,new_name):
        self.name = new_name
    def mod_id(self,new_id):
        self.id = new_id
class guvi(emp):
    def display(self):
        print("hi my id G"+str(self.id),"\nmy name ",self.name,"\nmy age",self.age)
e4=guvi(88,"aaa",5)
e4.display()


    

