# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      q = deque()
      ans = []
      if root ==  None:
        return []  
      q.append((0,root))

      while q:
        i,ele = q.popleft()
        while i>len(ans)-1:
            ans.append([])
        ans[i].append(ele.val)
        if ele.left:
            q.append((i+1,ele.left))
        if ele.right:
            q.append((i+1,ele.right))

      return ans  