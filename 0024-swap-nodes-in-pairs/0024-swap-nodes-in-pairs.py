# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        ptr = head
        ptr2 = head.next


        while  True:
            ptr.val ,ptr2.val = ptr2.val,ptr.val

            if ptr.next.next:
                ptr = ptr.next.next
            else:
                break
            if ptr2.next.next:
                ptr2 = ptr2.next.next
            else:
                break
        return head