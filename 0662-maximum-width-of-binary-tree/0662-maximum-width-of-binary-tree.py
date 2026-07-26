# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()

        q.append([root ,1])
        ans = 0
        while q:
            q1 = deque()
            while q:
                ele = q.popleft()
                if ele[0].left:
                    q1.append([ele[0].left , ele[1]*2])
                if ele[0].right:
                    q1.append([ele[0].right , ele[1]*2+1])
            if q1:
                ans = max(ans ,q1[-1][1] - q1[0][1])
            q = q1
        return ans+1
                
