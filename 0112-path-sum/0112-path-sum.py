class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(node, summ):
            if node is None:
                return False

            summ += node.val

            if node.left is None and node.right is None:
                return summ == targetSum

            return helper(node.left, summ) or helper(node.right, summ)

        return helper(root, 0)