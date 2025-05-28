# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def middle(head):
            temp = ListNode(0)
            temp.next = head

            ptr = temp
            ptr2 = head
            while ptr2 != None and ptr2.next != None:
                ptr = ptr.next
                ptr2 = ptr2.next.next

            return ptr

        def merge(l1, l2):
            ptr = l1
            ptr2 = l2
            l3 = ListNode(0)
            ptr3 = l3

            while ptr != None and ptr2 != None:
                if ptr.val <= ptr2.val:
                    ptr3.next = ptr
                    temp = ptr
                    ptr = ptr.next
                    temp.next = None
                    ptr3 = ptr3.next
                else:
                    ptr3.next = ptr2
                    temp = ptr2
                    ptr2 = ptr2.next
                    temp.next = None
                    ptr3 = ptr3.next

            if ptr == None:
                if ptr2 != None:
                    ptr3.next = ptr2
            elif ptr2 == None:
                if ptr != None:
                    ptr3.next = ptr

            return l3.next

        def divide(head):
            if head == None or head.next == None:
                return head

            mid = middle(head)
            temp = mid.next
            mid.next = None

            a1 = divide(head)
            a2 = divide(temp)

            return merge(a1, a2)

        return divide(head)
