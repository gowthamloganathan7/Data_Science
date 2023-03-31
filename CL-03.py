# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:32:22 2023

@author: Gowtham
"""

###########               """ TUPLE"""                            #############
id =(23,55,66,99)
id,type(id)

id[2]

id = (55,66,10,25,30,40,99)

name = ("karthick","gowtham","anto","karthick","karthick","anto")

len(name)

name.count("karthick")

name.count("aaa")

name.index("karthick")
name.index("gowtham")
print(name.index("anto")) #it will print the first index value in the tuple
 
name[1:-1][0] #it first take value from 1 to -1 and it will take 0th index value from it

name1 =("nlg","rahul")

name2 = name+name1+("mukunth","niranjan")
print(name2)


##################  """"""""""LIST""""""""""""""""" #########################

#changeable,order,duplicates aloowed

name = ["karthick","gowtham","anto","karthick","karthick","anto"]

#append
name.append("rahul")
name
#insert
name.insert(3,"anu") # 3 is the poistion where we need to insert
                     # ANU is the thing which need to be add on the place
name
#copy
x= name.copy()
x
#count
name.count("karthick")
#index
name.index("gowtham")
#clear
#y= name.clear()
#y
#pop
name.pop() #it will remove the last value from the list
print(name)
name.pop(2) #it will remove the second index value
name
#name.pop("anu") #it will not take the str value
name
#remove
name.remove("karthick") #it will remove the value which we given
name

data =[1,2,3,4,5]
data.pop(2) #it will takes only index value to remove
data

#reverse
name.reverse() #it will reverse the list
name
#sort
name.sort() # it will sort the list by numerical, uppercase, lowercase
name

name[1:3]="nlg"
name


################## """"Dictionary""""""""  ###########################

#change, unordered, in values duplicates allowed, key duplicates not allowed 

