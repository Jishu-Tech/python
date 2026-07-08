class stack:
    def __init__(self):
        self.top = -1
        self.stk=[0]*8
        self.size=8

    def push(self,item):
        if self.top==self.size-1:
            print("stack is full")
        else:
            self.top+=1
            self.stk[self.top]=item

    def pop(self):
        if self.top== -1:
            print("Stack is under fllow")

        else:
            item=self.stk[self.top]
            self.top-=1
            return item


    def display(self):
        if self.top== -1:
            print("stack is under flow")
        else:
            for i in range(0,self.top+1):
                print(self.stk[i])




obj=stack()
obj.push(10)
obj.push(20)
print("the deleted item is", obj.pop())
#obj.display()
obj.push(30)
obj.display()

        
