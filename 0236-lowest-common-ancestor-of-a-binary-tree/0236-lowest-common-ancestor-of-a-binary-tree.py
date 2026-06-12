# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        m = {}
        qu = deque()

        qu.append(root)
        
        while qu:
            a = qu.popleft()
            if a.left:
                m[a.left] = a
                qu.append(a.left)
            if a.right:
                m[a.right] = a
                qu.append(a.right)

        s = set()
        temp = p
        s.add(temp)
        while temp in m:
            s.add(m[temp])
            temp = m[temp]
        temp2 = q
        while temp2 in m:
            if temp2 in s:
                return temp2
            else:
                temp2 = m[temp2]
        return root