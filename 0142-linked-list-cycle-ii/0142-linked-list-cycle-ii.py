class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ptr = head
        ptr2 = head

        ptr3 = head


        while ptr2 != None and ptr2.next != None:
            ptr = ptr.next
            ptr2 = ptr2.next.next
            if ptr == ptr2:
                while ptr3 != ptr2:
                    ptr3 = ptr3.next
                    ptr2 = ptr2.next
                    
                return ptr3

        return None


                