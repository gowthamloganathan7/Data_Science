class node:#2#13
    def __init__(self,data):#3#14
        self.left = None #4#15
        self.data = data #5#16
        self.right = None #6#17
    def insertValue(self,newdata):#8#20
        if self.data: #9#21
            if newdata<self.data: #10#
                if self.left is None: #11
                    self.left = node(newdata) #12#18
                else:
                    self.left.insertValue(newdata)
            elif newdata>self.data:
                if self.right is None:
                    self.right = node(newdata)
                else:
                    self.right.insertValue(newdata)
        else:
            self.data = newdata
    def show(self):
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()
        
        
        
        
root = node(111) #1 
root.insertValue(100) #7
root.insertValue(1)#19
root.insertValue(0)
root.insertValue(30)
root.insertValue(45)
root.insertValue(50)
root.insertValue(99)
root.insertValue(67)
root.insertValue(150)
root.insertValue(112)
root.insertValue(300)
root.insertValue(1100)

root.show()

#1 - so we are creating a ref node = 100
#2 - root object is create based on node class
#3 - self = root , data = 111
#4 - self.left = root.left => None
#5 - self.data = root.data => 111
#6 - self.right = root.right => None
#7 - inserting a new node
#8 - self - root, newdata = 100
#9 - self.data = root.data = 111
#10 - newdata<self.data = 100<root.data= 111 => 100<111
#11 - self.left = root.left -> root.left = none
#12 - overwriting self.left =root.left -> node(100)
#13 - so it will goes to class node
#14 - self = root.left, data= 100
#15 - self.left - root.left = None
#16 - self.data - root.data = 100
#17 - self.right - root.data = None
#18 - self.left = 110.left = 100
#19 - new data = 1
#20 - self = root, newdata = 1
#21 - 




   
