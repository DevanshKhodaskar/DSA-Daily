# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr = head
        ptr2 = head
        a = []  
        
        while ptr!=None:
            a.append(ptr.val)
            ptr = ptr.next
        print(a)

        a.sort()
        while ptr2!=None:
            ptr2.val = a[0]
            a.pop(0)
            
            ptr2 = ptr2.next

        return head