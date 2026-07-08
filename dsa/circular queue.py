class CQueue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.queue = [0] * 8
        self.size = 8

    def insertion(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            #print(item)

    def deletion(self):
        if self.front == -1:
            print("Queue is underflow")
        else:
            item = self.queue[self.front]
            print("\n",item, "deleted")

            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Queue elements:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            #print()



obj = CQueue()

obj.insertion(10)
obj.insertion(20)
obj.insertion(30)

obj.display()

obj.deletion()
obj.display()
obj.insertion(40)
obj.display()

obj.deletion()
obj.display()
