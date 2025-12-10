# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        stack = []
        stack.append(root)

        while stack:
            a = stack.pop()
            z = a.val
            node = self.search(root,k-z)
            if node and node is not a:
                return True
            else:
                if a.left is not None:
                    stack.append(a.left) 
                if a.right is not None:
                    stack.append(a.right) 

        return False

    def search(self,root,val):
        z = root
        while z != None:
            if z.val == val:
                return z
            if z.val>val:
                z = z.left
            else:
                z = z.right

        return False
        