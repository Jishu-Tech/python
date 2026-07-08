class node:
    def __init__(self,item):
        self.info=item
        self.right = None
        self.left = None

class BinarySTree:
    def __init__(self):
        self.root = None
    def insert(self,item):
        nd = node(item)
        if self.root == None:
            self.root = nd
            return
        temp = self.root
        while temp!= None:
            if item<temp.info:
                parant = temp
                temp = temp.left
            else:
                parant = temp
                temp = temp.right
        if item<parant.info:
            parant.left=nd
        else:
            parant.right = nd

def inorder(nd):
    if nd!=None:
        inorder(nd.left)
        print(nd.info)
        inorder(nd.right)
        
def preorder(nd):
    if nd!=None:
        print(nd.info)
        preorder(nd.left)
        preorder(nd.right)

def postorder(nd):
    if nd!=None:
        postorder(nd.left)
        postorder(nd.right)
        print(nd.info)
        



obj=BinarySTree()
obj.insert(10)
obj.insert(5)
obj.insert(30)
obj.insert(25)
obj.insert(7)
obj.insert(2)
obj.insert(55)
inorder(obj.root)
print("preeorder")
preorder(obj.root)
print("postorder")
postorder(obj.root)            
