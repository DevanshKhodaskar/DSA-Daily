# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lst = self.helper(root)
        a = set()
        x = p
        y = q
        
        while x != root:
            a.add(x)
            x = lst[x]

        while y != root:
            if y in a:
                return y
            else:
                y = lst[y]
        return root
        




    def helper(self,root):
        #[child:parent]
        ans = {}
        stack = []
        stack.append(root)
        while stack:
            a = stack.pop()
            if a.left is not None:
                 ans[a.left] = a
                 stack.append(a.left)
            if a.right is not None:
                 ans[a.right] = a
                 stack.append(a.right)
        return ans



        