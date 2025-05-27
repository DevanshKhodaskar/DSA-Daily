# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        ptr = temp
        ptr2 = head

        if head == None:
            return None

        if head.next == None:
            return None
        # if head.next.next == None:
        #     head.next = head.next.next
        #     return head



        while ptr2 != None and ptr2.next != None:
            ptr = ptr.next
            ptr2 = ptr2.next.next

        ptr.next = ptr.next.next


        return head
        