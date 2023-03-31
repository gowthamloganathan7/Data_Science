

############################# LINKED LIST ####################################

class node: #2 so arg "gowtham" will comes here
    def __init__(self,data): #3 n1."gowtham" is passed here
        self.datavalue = data #4 n1.headvalue.datavalue = "gowtham"
        self.nextvalue = None #5 n1.headvalue.nextvalue = "gowtham"
class linkedlist:
    def __init__(self):
        self.headvalue=None
    def display(self):
        temp= self.headvalue
        while temp is not None:
            print(temp.datavalue)
            temp=temp.nextvalue
        

n1=linkedlist()   
n1.headvalue=node("gowtham")#1 passing arg to node class
n1.headvalue.datavalue

n2 =node("kavi")
n3 =node("naveen")
n4 =node("sathya")

n1.headvalue.nextvalue = n2
n2.nextvalue = n3
n3.nextvalue = n4

n1.display()
n4.datavalue

############ ########## """class 10"""" #####################################

class node: #creating a new node
    def __init__(self,data): 
        self.datavalue = data 
        self.nextvalue = None
class linkedlist: #creating a new linked list 
    def __init__(self): #creating a headvalue
        self.headvalue=None
    def display(self): #showing the values present the linked list
        temp= self.headvalue
        while temp is not None: 
            print(temp.datavalue)
            temp=temp.nextvalue 
    def insert_beg(self,new_data): #inserting new row in the begining
        tempnode = node(new_data)
        tempnode.nextvalue=self.headvalue
        self.headvalue=tempnode
    def insert_mid(self,middle_node,new_data): #insert in the new node in the middle
        tempnode = node(new_data)
        tempnode.nextvalue = middle_node.nextvalue
        middle_node.nextvalue = tempnode
    def cut(self,remove_data): #removing the node from the linked list
        temp = self.headvalue 
        while temp is not None: 
            if temp.datavalue == remove_data:
                break
            previousnode = temp
            temp = temp.nextvalue
        if temp == None:
            print("no such data")
            return
        if temp == self.headvalue:
            self.headvalue = temp.nextvalue            
        else: 
            previousnode.nextvalue = temp.nextvalue 
    def insert_end(self,new_data): #adding node into the linked list at end
        tempnode = node(new_data)
        temp = self.headvalue 
        while temp.nextvalue is not None:
            temp =temp.nextvalue 
        temp.nextvalue = tempnode
            
            

n1 = linkedlist()
n1.headvalue = node("gowtham") #1 
n1.headvalue.datavalue
n1.headvalue.nextvalue = node("kavi")
print('************before insert**************')
n1.display()
n1.insert_beg("karthi")
print('************after insert**************')
n1.display()
n1.insert_mid(n1.headvalue.nextvalue,"naveen")
print('************after insert middle**************')
n1.display()
n1.cut("karthi")
print("************** cut **************")
n1.display()
print("****************** insert_end**************")
n1.insert_end("sathish")
n1.display()
