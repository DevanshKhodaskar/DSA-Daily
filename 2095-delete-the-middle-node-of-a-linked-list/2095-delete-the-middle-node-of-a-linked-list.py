# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        low = head
        high = head.next
        if low == None or low.next == None:
            return None

        while high and high.next and high.next.next:
            low = low.next
            high = high.next.next
        
        low.next = low.next.next
        print(f"low:{low.val}")
        return head
        
        