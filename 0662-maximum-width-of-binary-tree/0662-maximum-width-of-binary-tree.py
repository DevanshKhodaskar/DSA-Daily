from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxx = 0
        q = deque([(root, 0)])

        while q:
            l = len(q)
            initial_node, initial_index = q[0]

            for i in range(l):
                node, index = q.popleft()

                if node.left:
                    q.append((node.left, 2 * index))
                if node.right:
                    q.append((node.right, 2 * index + 1))

            maxx = max(maxx, index - initial_index + 1)

        return maxx
