# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l1 = p if p.val<q.val else q
        l2 = p if p.val>q.val else q
        ans = root
        while True:
            if l2.val < ans.val:  
                ans = ans.left   
            elif l1.val > ans.val:
                ans = ans.right 
            else: return ans