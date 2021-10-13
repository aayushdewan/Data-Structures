class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def Insert(root, key):
    if root == None:
        new_node = Node(key)
        return new_node
    q = [root]
    while len(q):
        tmp = q[0]
        q.pop()
        if tmp.left==None:
            new_node = Node(key)
            tmp.left = new_node
            break
        else:
            q.append(tmp.left)
        if tmp.right == None:
            new_node = Node(key)
            tmp.right = new_node
            break
        else:
            q.append(tmp.right)

def heightOfNode(root, h, dit):
    if root!=None:
        heightOfNode(root.left, h+1, dit)
        dit[root.val] = h
        heightOfNode(root.right, h+1, dit)

def Level_Order_Traversal(root, dit):
    c = 0
    i = 0
    ls = []
    while c < len(dit):
        ls_in = []
        for k,v in dit.items():
            if v == i:
                ls_in.append(k)
                c = c+1
        ls.append(ls_in)
        i = i+1
    print(ls)



dit = {}
n1 = Node(10)
Insert(n1, 20)
Insert(n1, 30)
Insert(n1, 90)
heightOfNode(n1, 0, dit)
print(dit)
Level_Order_Traversal(n1, dit)