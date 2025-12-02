# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.postorderptr = 0

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

    
        postorder = postorder[::-1]

        head = TreeNode(postorder[0])
        self.postorderptr = 1
        self.helper(head, postorder, inorder)
        return head

    def helper(self, head: TreeNode, postorder: List[int], arr: List[int]):
        if not arr or self.postorderptr >= len(postorder):
            return

        for i in range(len(arr)):
            if arr[i] == head.val:
                id = i
                break

        l1 = arr[:id]     
        l2 = arr[id + 1:]  

       
        if l2 and self.postorderptr < len(postorder):
            v_right = postorder[self.postorderptr]
            self.postorderptr += 1
            rnode = TreeNode(v_right)
            head.right = rnode
            self.helper(rnode, postorder, l2)


        if l1 and self.postorderptr < len(postorder):
            v_left = postorder[self.postorderptr]
            self.postorderptr += 1
            lnode = TreeNode(v_left)
            head.left = lnode
            self.helper(lnode, postorder, l1)
