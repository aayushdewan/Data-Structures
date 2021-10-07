class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def Insert(head, n):
    if head.next == None:
        head.next = n
        n.prev = head
    else:
        Insert(head.next, n)

def Print(head):
    while head:
        print(head.val, end=' ')
        head = head.next

def Reverse(p, c, n):
    while c:
        c.next = p
        c.prev = n
        p = c
        c = n
        if n:
            n = n.next
    return p





root = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)
Insert(root, n1)
Insert(root, n2)
Insert(root, n3)
Insert(root, n4)

Print(root)
print()
p = None
c = root
n = root.next
head_new = Reverse(p,c,n)
#print(head_new.val)
Print(head_new)

