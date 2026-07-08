class  node:
    def __init__(self,item):
        self.info =item
        self.next = None
        self.prev = None


class DlinkedList:
    def __init__(self):
        self.start = None

    def insert_at_last(self,item):
        nd=node(item)
        if self.start == None:
            self.start = nd
            return
        temp =  self.start
        while temp.next is not None:
            temp =temp.next
        temp.next= nd
        nd.prev = temp

    def insert_at_beg(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            return
        self.start.prev=nd
        nd.next=self.start
        self.start=nd


    def insert_end_pos(self,item,pos):
        if pos==1:
            self.insert_at_beg(item)
        else:
            nd=node(item)
            i=1
            temp=self.start
            while temp.next != None:
                self.prev = temp
                temp=temp.next
                i=i+1
                if temp.next == None:
                    temp.next=nd
                    return
                nd.prev=temp
                    
                    
               
                
                

    def display(self):
        temp =  self.start
        while temp != None:
            print(temp.info)
            temp =temp.next

obj = DlinkedList()
obj.insert_at_last(30)
obj.insert_at_last(40)
obj.insert_at_beg(20)
obj.insert_end_pos(10,3)
obj.display()
