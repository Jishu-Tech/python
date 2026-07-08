class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    def insert(self, coeff, power):
        new_node = Node(coeff, power)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head

        while temp:
            print(f"{temp.coeff}x^{temp.power}", end="")

            if temp.next:
                print(" + ", end="")

            temp = temp.next

        print()


# Create polynomial
p = Polynomial()

# Insert terms
p.insert(5, 3)
p.insert(4, 2)
p.insert(-7, 1)
p.insert(9, 0)

# Display polynomial
p.display()
