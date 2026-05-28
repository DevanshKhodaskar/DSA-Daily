# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None or head.next.next == None:
            return head

        # count nodes
        count = 0
        curr = head
        while curr != None:
            count += 1
            curr = curr.next

        evenCount = count // 2

        p1 = head
        p2 = head

        # original tail
        while p1.next != None:
            p1 = p1.next

        # move even nodes
        while evenCount > 0:

            temp = p2.next

            p2.next = temp.next

            p1.next = temp
            p1 = temp

            temp.next = None

            p2 = p2.next

            evenCount -= 1

        return head