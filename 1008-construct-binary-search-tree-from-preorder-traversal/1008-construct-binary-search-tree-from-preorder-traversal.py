# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        return self.helper(preorder)

    def helper(self,preorder):
        if len(preorder)==0:
            return None

        a = preorder[0]
        i = 1
        while i < len(preorder) and preorder[i] < a:
            i += 1

        ans = TreeNode(a)
        ans.left = self.helper(preorder[1:i])
        ans.right =self.helper(preorder[i:])
        return ans
        

        