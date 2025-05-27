# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        ptr2 = head

        if head.next == None:
            return None

        if head.next.next == None:
            if n == 2:
                return head.next
            elif n == 1:
                head.next = None
                return head

        count = 0
        while ptr2 != None:
            ptr2 = ptr2.next 
            count+=1
        print(f"count:{count}")

        temp = count - n
        if n == count:
            return head.next

        for i in range(temp-1):
            print(f"ptr.val:{ptr.val}")
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head
        
        