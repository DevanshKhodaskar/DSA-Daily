# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        memo = {}
        memo[1] = [TreeNode(0)]
        def helper(n):
            if n in memo:
                return memo[n]
            else:
                ans = []
                for i in range(1,n,2):
                    for left in helper(i):
                        for right in helper(n-i-1):
                            root = TreeNode(0)
                            root.left = left
                            root.right = right
                            ans.append(root)
                memo[n] = ans
                return memo[n]
        
        return helper(n)
                    


           