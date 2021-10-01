class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def Insert(root, new_node):
    if new_node.val < root.val:
        if root.left == None:
            root.left = new_node
        else:
            Insert(root.left, new_node)
    else:
        if root.right == None:
            root.right = new_node
        else:
            Insert(root.right, new_node)

def PrintTree(root):
    if root == None:
        return
    else:
        PrintTree(root.left)
        print(root.val, end=' ')
        PrintTree(root.right)

def Find_Node(root,node):
    if root==None:
        return None
    elif root.val == node.val:
        return root
    elif node.val < root.val:
        return Find_Node(root.left, node)
    elif node.val > root.val:
        return Find_Node(root.right, node)
    else:
        return None

n1 = Node(50)
n2 = Node(30)
n3 = Node(70)
n4 = Node(40)
n5 = Node(60)
n6 = Node(90)
n7 = Node(100)
Insert(n1, n2)
Insert(n1, n3)
Insert(n1, n4)
Insert(n1, n5)
Insert(n1, n6)
PrintTree(n1)
if(Find_Node(n1,n7)):
    print("The value is", n7.val)
else:
    print("Sorry No Such value")

