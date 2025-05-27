# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = ListNode()
        ptr2 = ListNode()

        p1 = ptr
        p2 = ptr2

        temp = head
        count = 0
        while temp != None:
            if count%2 == 0:
                p2.next = temp
                p2 = p2.next

            else:
                p1.next = temp
                p1 = p1.next
            count+=1
            temp = temp.next
        # if head.val%2 != 0:
        #     new_head = ptr.next
        #     p1.next = ptr2.next
        #     p2.next = None
        # else:
        new_head = ptr2.next
        p2.next = ptr.next
        p1.next = None
        return new_head
        
        