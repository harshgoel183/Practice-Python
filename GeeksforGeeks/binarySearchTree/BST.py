class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inoder(root):
    if root:
        inoder(root.left)
        print(root.data)
        inoder(root.right)


def search(root,key):
    if root.data == key or root is None:
        print("Found "+str(root.data))
        return root

    if root.data < key:
        return search(root.right,key)

    return search(root.left,key)

r = Node(50)
insert(r,Node(20))
insert(r,Node(30))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(10))

inoder(r)

search(r,60)