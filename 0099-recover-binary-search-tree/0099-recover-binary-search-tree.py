from typing import Optional
from collections import deque

class Solution:
    def recoverTree(self, root: Optional['TreeNode']) -> None:
        p = []
        ans = self.inorder(root)
        for i in range(len(ans) - 1):
            if ans[i].val > ans[i + 1].val:
                p.append(ans[i])
                p.append(ans[i + 1])

        if not p:
            return

        first = p[0]
        second = p[-1]
        first.val, second.val = second.val, first.val

    def inorder(self, root: Optional['TreeNode']):
        stack = []
        ans = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans.append(node)
            node = node.right
        return ans
