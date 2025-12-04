# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
           return TreeNode(val)
        self.helper(root,val)
        return root

    def helper(self,root,val):
       
    
       


        if val>root.val and root.right:
           
            self.helper(root.right,val)


        elif val>root.val and not root.right:
           
            root.right = TreeNode(val)    

        elif val<root.val and root.left:
           
            self.helper(root.left,val)


        elif val<root.val and  not root.left:
       
            root.left = TreeNode(val)    

        

        
        