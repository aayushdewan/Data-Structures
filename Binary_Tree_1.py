# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    if root == None:
        return []
    if root.left == None and root.right == None:
        return [root.value]
    ls = []
    ls2 = []

    def Check(root, v, ls):
        if root == None:
            return
        if root.left == None and root.right == None:  # Check the leaf node and add teh value of the leaf node
            v = v + root.value
            ls.append(v)  # append the sum of branch from root
            return
        v = v + root.value  # root -> left -> right
        Check(root.left, v, ls)
        Check(root.right, v, ls)
        print(ls)
        return ls

    ls2 = Check(root, 0, ls)
    return ls2



