# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = []
        q.append(root)
        q.append(root)
        while len(q) != 0:
            v1 = q.pop(0)
            v2 = q.pop(0)
            if v1 == None and v2 == None:
                continue
            if v1 == None or v2 == None:
                return False
            if v1.val != v2.val:
                return False
            q.append(v1.left)
            q.append(v2.right)
            q.append(v1.right)
            q.append(v2.left)

        return True
