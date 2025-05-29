# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        if not head :
            return None
        if k == 0 or head.next == None:
            return head

        ptr = head
        while ptr:
            ptr = ptr.next
            n+=1

        if k%n == 0:
            return head
        ptr = head
        for i in range(1,n-(k%n)):

            ptr = ptr.next

        ptr2 = ptr.next

        ptr3 = ptr2
        print(f"ptr2:{ptr2.val} | ptr :{ptr.val} | ptr3:{ptr3.val}")
        while ptr3.next!= None:
            ptr3= ptr3.next

        ptr.next = None
        ptr3.next = head
        return ptr2
    
        