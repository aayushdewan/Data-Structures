class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
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

def Height(root, h, dit):
    if root!=None:
        Height(root.left, h+1, dit)
        dit[root.val] = h
        Height(root.right, h+1, dit)



def Inorder(root):
    if root!=None:
        Inorder(root.left)
        print(root.val, end=" ")
        Inorder(root.right)




# def Height(root, h, dit):
#     if root!=None:
#         Height(root.left, h+1, dit)
#         dit[root.val] = h
#         Height(root.right, h+1, dit)

dit = {}
n1 = Node(10)
Insert(n1, 20)
Insert(n1, 30)
Insert(n1, 40)
Insert(n1, 50)
Inorder(n1)
Height(n1, 0, dit)
print(dit)
ls = []
i = 0
c = 0
while c != len(dit):
    ls_in = []
    for k, v in dit.items():
        if v == i:
            ls_in.append(k)
            c = c + 1
    i = i+1
    ls.append(ls_in)
ls = ls[::-1]
print(ls)


