class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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

def Mode_In_BST(root, dit):
    if root!=None:
        Mode_In_BST(root.left, dit)
        try:
            dit[root.val]+=1
        except:
            dit[root.val]=1
        Mode_In_BST(root.right, dit)



dit = {}
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(20)
n5 = Node(30)
n6 = Node(20)
Insert(n1, n2)
Insert(n1, n3)
Insert(n1, n4)
Insert(n1, n5)
Insert(n1, n6)


Mode_In_BST(n1, dit)
print(dit)
max_count = max(dit.values()) # O(n)
print(max_count)
for k, v in dit.items():
    if v == max_count:
        print("The mode value is", k)
        break


