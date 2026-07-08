class node:
    def __init__(self, item):
        self.info = item
        self.right = None
        self.left = None


class BinaryStree:
    def __init__(self):
        self.root = None

    def insert(self, item):
        nd = node(item)

        if self.root is None:
            self.root = nd
            return

        temp = self.root

        while temp is not None:

            if item < temp.info:
                parent = temp
                temp = temp.left

            else:
                parent = temp
                temp = temp.right

        if item < parent.info:
            parent.left = nd
        else:
            parent.right = nd

    def inorder(self, nd):

        if nd is not None:
            self.inorder(nd.left)
            print(nd.info)
            self.inorder(nd.right)

    def inorder_succer(self,nd):
        temp=nd
        succ.par = temp
        succ = nd.right
        while succ.left != None:
            succ.par = succ
            succ = succ.left
        return succ_par, succ

   
    # ---------------- SEARCH ----------------

    def serch(self, item):

        if self.root is None:
            print("Empty")
            return None, None
        if self.root == item:
            print("found")
            return

        temp = self.root
        par = temp

        while temp is not None:

            if item == temp.info:
                print("Found")
                return par, temp

            elif item < temp.info:
                par = temp
                temp = temp.left

            else:
                par = temp
                temp = temp.right
        if temp == None:
            print("Not found")
        return par, temp

    # ---------------- DELETION ----------------

    def deletion(self, item):

        if self.root is None:
            print("Empty tree")
            return

        par, temp = self.serch(item)

        if temp is None:
            print("Item not found")
            return

        # if the node has zero child

        if temp.left is None and temp.right is None:

            if par == temp:
                del temp
                self.root = None

            elif temp.info < par.info:
                par.left = None

            else:
                par.right = None

            del temp

        # if the deleted node have  left child only

        elif temp.left is not None and temp.right is None:

            if par == temp:
                self.root = temp.left
                del temp

            if temp.info > par.info:
                par.right = temp.left
                

            elif temp.info < par.info:
                par.left = temp.left

            del temp

        # if the deleted node have  right child only

        elif temp.right is not None and temp.left is None:

            if par == temp:
                self.root = temp.right

            elif temp.info > par.info:
                par.left = temp.right

            elif temp.info < par.info:
                par.right = temp.right

            del temp

        #if the deleted node both child

        else:
            succ_par,succ = self.inorder_succer(temp)
            temp.info=succ.info
            if succ_par.left == succ:
                succ_par.left = succ.right
            else:
                succ_par.right= succ.right
            del succ
       


obj = BinaryStree()

obj.insert(10)
obj.insert(20)
obj.insert(15)
print("tree is ")
obj.inorder(obj.root)
print("serch value is 20")
obj.serch(20)

print("Before deletion:")
obj.inorder(obj.root)

obj.deletion(15)

print("After deletion:")
obj.inorder(obj.root)
