class node:
    def __init__(self,item):
        self.info = item
        self.next = None


class slinkedList:
    def __init__(self):
        self.start = None

    #  insert at last
    def insert_at_last(self,item):
        nd = node(item)

        if self.start == None:
            self.start = nd
            return

        temp = self.start
        while temp.next != None:
            temp = temp.next

        temp.next = nd


    #  delete first
    def delete_start_node(self):
       if self.start is None:
        print("List is empty")
        return
    
       temp = self.start        # Save the current head
       self.start = temp.next   # Move the head pointer to the next node
       del temp    


    #  delete last
    def delete_last_node(self):
        if self.start == None:
            print("List is empty")
            return

        temp = self.start

        if temp.next == None:
            self.start = None
            return

        while temp.next != None:
            prev = temp
            temp = temp.next

        prev.next = None
        del temp


    #  delete by value
    def delete_value(self, item):
        if self.start == None:
            print("List is empty")
            return

        if self.start.info == item:
            temp = self.start
            self.start = temp.next
            del temp
            return

        temp = self.start

        while temp.next != None:
            if temp.next.info == item:
                d = temp.next
                temp.next = d.next
                del d
                return
            temp = temp.next

        print("Item not found")


    #  delete by position
    def delete_position(self, pos):
        if self.start == None:
            print("List is empty")
            return

        if pos == 1:
            temp = self.start
            self.start = temp.next
            del temp
            return

        temp = self.start
        i = 1

        while temp.next != None and i < pos - 1:
            temp = temp.next
            i = i + 1

        if temp.next == None:
            print("Position out of range")
            return

        d = temp.next
        temp.next = d.next
        del d


    #  display
    def display(self):
        temp = self.start
        while temp != None:
            print(temp.info)
            temp = temp.next


#  MAIN
obj = slinkedList()

# create list
obj.insert_at_last(10)
obj.insert_at_last(20)
obj.insert_at_last(30)
obj.insert_at_last(40)
obj.insert_at_last(50)

print("Original:")
obj.display()

print("\nDelete first:")
obj.delete_start_node()
obj.display()

print("\nDelete last:")
obj.delete_last_node()
obj.display()

print("\nDelete value 30:")
obj.delete_value(30)
obj.display()

print("\nDelete position 2:")
obj.delete_position(2)
obj.display()
