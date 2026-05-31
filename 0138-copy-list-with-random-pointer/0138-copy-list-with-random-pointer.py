"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        dic = defaultdict(Node)
        h1 = head
        newhead = Node(h1.val)
        ans = newhead
        dic[h1] = newhead
        while h1.next!=None:
            h1 = h1.next
            temp = Node(h1.val)
          
            newhead.next = temp
            newhead = newhead.next
            dic[h1] = newhead
        h2 = head
        h3 = ans
        print(f"{h1.val}\t{dic[h1].val}")
        while h2!= None:
            h3.random = dic[h2.random] if h2.random else None
            h2 = h2.next
            h3 = h3.next
        return ans
        