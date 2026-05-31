# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next ==  None or k == 0:
            return head
        

        h1 = head
        n = 0
        while h1.next:
            h1 = h1.next
            n+=1
        
        n+=1
        k = k%n
        if k == 0:
            return head
        t = n-k
        h2 = head
        t = t-1 if t>0 else t
        
        for i in range(t):
            h2 = h2.next
        h3 = h2.next
        h2.next = None
        h1.next = head
        return h3