# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preorderptr = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode()
        head.val = preorder[0]
        self.preorderptr+=1
        self.helper(head,preorder,inorder)
        return head



        

    def helper(self,head,preorder,arr):
        if not arr:
            return

        else:
            for i in range(len(arr)):
                if arr[i] == head.val:
                    id = i
                    break
            l1 = arr[:id]
            l2 = arr[id+1:]

            if l1:
                vl = preorder[self.preorderptr]
                self.preorderptr+=1
                lnode = TreeNode()
                lnode.val = vl
                head.left = lnode
                self.helper(lnode,preorder,l1)
            if l2:
                v2 = preorder[self.preorderptr]
                self.preorderptr+=1
                rnode = TreeNode()
                rnode.val = v2
                head.right = rnode
                self.helper(rnode,preorder,l2)
            