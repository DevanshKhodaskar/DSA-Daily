from collections import deque
from typing import Optional, List


class Solution:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.ans = []

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        self.q1.append(root)

        while self.q1 or self.q2:
            self.helper()

        return self.ans

    def helper(self):
        if self.q1:
            temp = []
            while self.q1:
                a = self.q1.popleft()
                temp.append(a.val)
                if a.left:
                    self.q2.append(a.left)
                if a.right:
                    self.q2.append(a.right)
            self.ans.append(temp)

        elif self.q2:
            temp = []
            while self.q2:
                b = self.q2.pop()
                temp.append(b.val)
               
                if b.right:
                    self.q1.appendleft(b.right)
                if b.left:
                    self.q1.appendleft(b.left)
            self.ans.append(temp)
