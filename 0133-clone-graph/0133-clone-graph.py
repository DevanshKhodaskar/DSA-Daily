"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import defaultdict,deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        m = defaultdict()
        if node  == None:
            return None
        r2 = Node()
        r2.val = node.val
        m[node]   = r2
        q =deque()

        q.append(node)

        while q:
            x = q.popleft()

            for i in x.neighbors:
                if i not in m:
                    temp = Node(i.val)
                    m[i] = temp
                    q.append(i)

                m[x].neighbors.append(m[i])

        return r2