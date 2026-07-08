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


    def insert_at_begain(self,item):
        nd = node(item)
        nd.next = self.start
        self.start = nd


     def insert_end_position(self, item, pos):
        if pos == 1:
            self.insert_at_begain(item)
        else:
            nd = node(item)
            i = 1
            temp = self.start

            while temp.next != None and i < pos:
                temp = temp.next
                i = i + 1

            if temp.next == None:
                temp.next = nd
                return


    # ✅ FIXED (separate function)
    def insert_after_item(self, item, key):
        if self.start == None:
            print("List is empty")
            return

        nd = node(item)
        temp = self.start

        while temp != None:
            if temp.info == key:
                nd.next = temp.next
                temp.next = nd
                return
            temp = temp.next

        print("Item not found")


    def display(self):
        temp = self.start
        while temp != None:
            print(temp.info)
            temp = temp.next



obj = slinkedList()
obj.insert_at_last(10)
obj.insert_at_last(20)
obj.insert_at_last(10)
obj.display()

obj.insert_at_begain(29)

obj.insert_at_last(40)

obj.insert_end_position(50,2)

# test after item
obj.insert_after_item(25,20)

obj.display()