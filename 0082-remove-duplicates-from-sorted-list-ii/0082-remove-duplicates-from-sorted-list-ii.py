# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        h1 = ListNode(-1)
        ans = h1
        h1.next = head

        h2 = head
        h3 = head.next

        while h3 is not None:
            if h2.val == h3.val:
                while h3 is not None and h2.val == h3.val:
                    h3 = h3.next

                h1.next = h3
                h2 = h3

                if h3 is not None:
                    h3 = h3.next

            else:
                h1 = h2
                h2 = h3
                h3 = h3.next

        return ans.next