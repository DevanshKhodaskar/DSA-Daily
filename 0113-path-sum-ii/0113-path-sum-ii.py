# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        final_ans = []

        def helper(root, summ, arr):
            if root is None:
                return

            summ += root.val
            arr = arr + [root.val]

            if root.left is None and root.right is None:
                if summ == targetSum:
                    final_ans.append(arr)
                return

            helper(root.left, summ, arr)
            helper(root.right, summ, arr)

        helper(root, 0, [])
        return final_ans