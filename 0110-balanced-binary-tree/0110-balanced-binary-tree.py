# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        else:

            temp =  abs(self.helper(root.left,1)-(self.helper(root.right,1)))

        if temp>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

        


    def helper(self,root,height):
        if root == None:
            return height
        else:
            return max(self.helper(root.left,height+1),self.helper(root.right,height+1))



        
        