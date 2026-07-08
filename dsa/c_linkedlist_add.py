class  node:
    def __init__(self,item):
        self.info =item
        self.next = None
class ClinkedList:
    def __init__(self):
        self.start = None

    def insert_at_last(self,item):
        nd=node(item)
        if self.start ==None:
            self.start = nd
            nd.next = self.start
            return
        temp = self.start
        while temp.next != self.start:
            temp=temp.next

        temp.next=nd
        nd.next=self.start
        

    def insert_at_beg(self,item):
        nd = node(item)
        if self.start == None:
            self.start = nd
            nd.next = nd
            return
        temp =self.start
        while temp.next != self.start:
            temp=temp.next
        nd.next=self.start
        temp.next=nd
        self.start=nd
    
    def delete_at_last(self):
        temp = self.start
        if temp.next==temp:
            return
        while temp.next.next != self.start:
           temp = temp.next

        temp.next = self.start
        
    def delete_at_beg(self):
        if self.start is None:
            return
        temp = self.start
        if temp.next == self.start:
           self.start = None
           del temp
           return
        last = self.start
        while last.next != self.start:
            last = last.next
        self.start = self.start.next
        last.next = self.start

        del temp

    

    def display(self):
        temp=self.start
        if self.start is None:
            print("List is empty")
            return
        while True:
            print(temp.info)
            temp = temp.next
            if temp == self.start:
                break


obj=ClinkedList()
obj.insert_at_last(10)
obj.insert_at_last(20)
obj.insert_at_beg(5)
obj.display()
print("the updated list is")
obj.delete_at_last()
obj.display()
print("the updated list is")
obj.delete_at_beg()
obj.display()
