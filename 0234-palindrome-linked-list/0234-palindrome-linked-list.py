class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []

        ptr = ptr2 = head

        while ptr2 and ptr2.next:
            s.append(ptr.val)
            ptr = ptr.next
            ptr2 = ptr2.next.next
        if ptr2:
            ptr = ptr.next
        
        while ptr!=None:
            temp = s.pop()
            if temp != ptr.val:
                return False
            ptr = ptr.next


        return True