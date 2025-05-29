# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head,k):
        if not head or not head.next:
            return head ,head

        ptr = head
        end = ptr
        ptr2 = ptr.next
        ptr3 = ptr2.next if ptr2 else None

        ptr.next = None 
        count = 1 
        while ptr2 is not None and count != k:
            ptr2.next = ptr
            ptr = ptr2
            ptr2 = ptr3
            if ptr3:
                ptr3 = ptr3.next
            count+=1

        return ptr ,end



    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        ptr = head
        last_end = None
        new_head = None
        while ptr != None:
            ptr2 = ptr
            for i in range(k):
                if ptr2 == None:
                    return new_head if new_head else head
                    
                ptr2 = ptr2.next

            start,end = self.reverse(ptr,k)
            if new_head == None:
                new_head = start
            end.next = ptr2
            if last_end:
                last_end.next = start
            last_end = end
            ptr = ptr2
        return new_head

        