class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        def breeak(head):
            ptr3 = head
            ptr = None
            ptr2 = head

            while ptr2 and ptr2.next:
                ptr = ptr3
                ptr3 = ptr3.next
                ptr2 = ptr2.next.next

            head2 = ptr3
            if ptr:
                ptr.next = None

            return head, head2

        def merge(head1, head2):
            ptr = head1
            ptr2 = head2

            head = ListNode(0)
            ans = head

            while ptr and ptr2:
                if ptr.val <= ptr2.val:
                    head.next = ptr
                    ptr = ptr.next
                else:
                    head.next = ptr2
                    ptr2 = ptr2.next
                head = head.next

            while ptr:
                head.next = ptr
                ptr = ptr.next
                head = head.next

            while ptr2:
                head.next = ptr2
                ptr2 = ptr2.next
                head = head.next

            return ans.next

        head1, head2 = breeak(head)

        left = self.sortList(head1)
        right = self.sortList(head2)

        return merge(left, right)
