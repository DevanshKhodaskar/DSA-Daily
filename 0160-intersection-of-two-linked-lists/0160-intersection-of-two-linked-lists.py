# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        a = []
        ptr = headA


        while ptr!=None:
            a.append(ptr)
            ptr = ptr.next


        ptr2 = headB
        while ptr2!=None:
            if ptr2 in a:
                return ptr2

            ptr2 = ptr2.next
        return None