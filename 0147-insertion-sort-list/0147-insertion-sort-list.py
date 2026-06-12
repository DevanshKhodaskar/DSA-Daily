# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(float("inf"))
        temp.next = head
        newHead = None
        
        while temp.next:
            ptr = temp
            ele = ptr
            val = float("-inf")

            while ptr.next:
                if val<ptr.next.val:
                    ele = ptr
                    val = ptr.next.val
                ptr = ptr.next

            least = ele.next
            ele.next = ele.next.next
            least.next = newHead
            newHead = least
        return newHead


