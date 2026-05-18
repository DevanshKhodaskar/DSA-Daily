# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next ==  None:
            return head
        
        if head.next.next ==  None:
            return head if head.val != head.next.val else head.next
        head1 = head
        head2 = head.next
        head3 = head.next.next

        

        while head3 !=None:
            if head3.val == head2.val:
                head1.next = head3
                head3 = head3.next
                head2 = head2.next
            else:
                head1 = head1.next
                head3 = head3.next
                head2 = head2.next
        return head if head.val != head.next.val else head.next