# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        
        ptr = headA
        ptr2 = headB


        while ptr != ptr2:
            if ptr == None:
                ptr = headB
            else:
                ptr = ptr.next

            if ptr2 == None:
                ptr2 = headA
            else:
                ptr2 = ptr2.next


        return ptr
            


        