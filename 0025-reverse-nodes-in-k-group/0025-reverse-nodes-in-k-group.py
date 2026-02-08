class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverseLL(head, tail):
            prev = None
            curr = head

            while curr != tail:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev, head

        ptr = head
        anshead = None
        ansTail = None

        while ptr:
            tail = ptr
            count = 0

            while count < k and tail:
                tail = tail.next
                count += 1

            if count < k:
                if ansTail:
                    ansTail.next = ptr
                break

            h1, t1 = reverseLL(ptr, tail)

            if not anshead:
                anshead = h1
                ansTail = t1
            else:
                ansTail.next = h1
                ansTail = t1

            ptr = tail

        return anshead if anshead else head
