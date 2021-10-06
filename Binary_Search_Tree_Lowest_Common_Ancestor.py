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
        print(root.val, end=' ')
        PrintTree(root.left)

        PrintTree(root.right)


def Lowest_Common_Ancestor(root, node1, node2):
    if root == None:
        return
    if root.val > node1.val and root.val > node2.val:
        return Lowest_Common_Ancestor(root.left, node1, node2)
    elif root.val < node1.val and root.val < node2.val:
        return Lowest_Common_Ancestor(root.right, node1, node2)
    else:
        print(root.val)
        return root



n = Node(0)
n1 = Node(7)
n2 = Node(2)
n3 = Node(9)
n4 = Node(1)
n5 = Node(5)
Insert(n1, n2)
Insert(n1, n3)
Insert(n1, n4)
Insert(n1, n5)
#Insert(n1, n6)
PrintTree(n1)
n = Lowest_Common_Ancestor(n1, n4, n5)
print(n.val)
