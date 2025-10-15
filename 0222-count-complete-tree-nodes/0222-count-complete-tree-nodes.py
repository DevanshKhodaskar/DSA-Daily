# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.ans
    

    def helper(self,root):
        if root == None:
            return
        else:
            self.ans+=1
            self.countNodes(root.left)
            self.countNodes(root.right)
        