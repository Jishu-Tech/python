class node:
    def __init__(self, item):
        self.info = item
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.start = None
        self.top = None

    def push(self, item):
        nd = node(item)

        if self.start is None:
            self.start = nd
            self.top = nd
            return

        self.top.next = nd
        self.top = nd

    def pop(self):
        if self.top is None:
            print("Stack Empty")
            return

        
        if self.start == self.top:
            x = self.top.info
            self.start = None
            self.top = None
            return x

        temp = self.start

        while temp.next != self.top:
            temp = temp.next

        x = self.top.info
        temp.next = None
        self.top = temp

        return x

    def display(self):
        if self.start is None:
            print("Stack Empty")
            return

        temp = self.start

        while temp is not None:
            print(temp.info, end=" ")
            temp = temp.next

        print()



s = StackLinkedList()

s.push(10)
s.push(20)
s.push(30)

print("Stack elements:")
s.display()

print("Deleted:", s.pop())

print("After pop:")
s.display()
