class node:
    def __init__(self,item):
        self.info = item
        self.next = None


class slinkedList:
    def __init__(self):
        self.start = None

    def insert_at_last(self,item):
        nd = node(item)

        if self.start == None:
            self.start = nd
            return
        temp = self.start
        while temp.next != None:
            temp = temp.next

        temp.next = nd

    def display(self):
        temp=self.start
        while temp!= None:
            print(temp.info)
            temp=temp.next

obj=slinkedList()
obj.insert_at_last(10)
obj.insert_at_last(20)
obj.insert_at_last(10)
obj.display()
