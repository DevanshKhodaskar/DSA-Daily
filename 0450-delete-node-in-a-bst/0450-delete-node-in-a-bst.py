# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if root.val == key:
            if root.right:
                x = self.leftmost(root)
                x.left = root.left
                x.right = root.right
                return x
            else:
                return root.left


        ptr = self.helper(root,key)
        # print(f"root.val:{ptr}")
        if ptr == None or ptr.val == None:
            return root
        


        if ptr.left and ptr.left.val == key:
            ptr2 = ptr.left
            x = self.rightmost(ptr2)
            if x == None:
                ptr.left = ptr2.right
                return root

            else:
                ptr.left = x
                x.left = ptr2.left
                x.right = ptr2.right
                return root

        if ptr.right and ptr.right.val == key:
            ptr2 = ptr.right
            x = self.leftmost(ptr2)
            if x == None:
                ptr.right = ptr2.left
                return root
            else:
                ptr.right = x
                x.left = ptr2.left
                x.right = ptr2.right
                return root


            
            




    def rightmost(self, root):
        if root.left is None:
            return None

        parent = root
        x = root.left
        while x.right is not None:
            parent = x
            x = x.right

       
        if parent is root:
            parent.left = x.left
        else:
            parent.right = x.left

        return x

    def leftmost(self, root):
        if root.right is None:
            return None

        parent = root
        x = root.right
        while x.left is not None:
            parent = x
            x = x.left

        if parent is root:
            parent.right = x.right
        else:
            parent.left = x.right

        return x
        
        

    def helper(self,root,val):
        if root ==  None:
            return None
        if (root.left and root.left.val == val) or(root.right and root.right.val == val):
            return root

        elif root.val>val:
            return self.helper(root.left,val)
        else:
            return self.helper(root.right,val) 
        