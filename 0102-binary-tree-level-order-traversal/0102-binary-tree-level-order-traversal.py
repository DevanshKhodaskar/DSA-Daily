# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root ==  None:
            return result

        q = deque()
        q.append(root)

        while q:
            temp = []

            for i in range(len(q)):
                ele = q.popleft()
                temp.append(ele.val)

                if ele.left:
                    q.append(ele.left)

                if ele.right:
                    q.append(ele.right)

            result.append(temp)
        return result
