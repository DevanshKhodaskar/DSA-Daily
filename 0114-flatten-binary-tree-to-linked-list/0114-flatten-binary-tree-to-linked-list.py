# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        a = deque()
        s = deque()
        s.append(root)

        while s:
            z = s.pop()
            a.append(z)
            s.append(z.right) if z.right else None
            s.append(z.left) if z.left else None
        
        for i in range(len(a)-1):
            a[i].right = a[i+1]
            a[i].left = None

        # a[-1].left = None
        # a[-1].right = None



        