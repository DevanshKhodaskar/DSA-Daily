# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        

        return self.helper(root1,root2)



    def helper(self,r1,r2):
        if r1 is None and r2 is None:
            return None

        else:
            if r1 is None:
                a  = TreeNode(r2.val)
                a.left = self.helper(None,r2.left)
                a.right = self.helper(None,r2.right)
                return a
             
            elif r2 is None:
                a  = TreeNode(r1.val)
                a.left = self.helper(r1.left,None)
                a.right = self.helper(r1.right,None)
                return a   
            else:
                a = TreeNode(r1.val + r2.val)
                a.left = self.helper(r1.left,r2.left)
                a.right = self.helper(r1.right,r2.right)
                return a
