# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head  ==None or head.next == None:
            return head
        h1= head
        h2 = head.next
        h3 = head.next.next
        h1.next= None

        while  h3:
            h2.next = h1
            h1 = h2
            h2 = h3
            h3 = h3.next

        h2.next = h1
        return h2