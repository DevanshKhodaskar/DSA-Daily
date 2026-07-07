# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict ,deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        paths = defaultdict(list)

        q = deque()

        q.append(root)

        while q:
            e = q.popleft()
            if e.left:
                paths[e.val].append(e.left)
                paths[e.left.val].append(e)
                q.append(e.left)
            if e.right:
                paths[e.val].append(e.right)
                paths[e.right.val].append(e)
                q.append(e.right)
        visited = set()

        q = deque()
        q.append((start , 0))
        ans = 0
        while q:
            ele , dep = q.popleft()
            visited.add(ele)
            ans = max(ans , dep)
            for i in paths[ele]:
                if i.val not in visited:
                    q.append((i.val , dep+1))
        return ans




        
        