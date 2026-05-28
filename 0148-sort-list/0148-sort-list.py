# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        

        p1 = head
        p2 = head.next 
        p3 = head.next.next

        def breeak(head):
            if not head or not head.next:
                return head,None
            p1 = head
            p2 = head
            p = ListNode(0)
            p.next = head
            while p1 and p1.next:
                p2 = p2.next
                p = p.next
                p1 = p1.next.next

            if p1 == None:
                p.next = None
                h1 = head
                h2 = p2
            else:
                h2 = p2.next
                h1 = head
                p2.next = None
            return h1,h2
        
        def merge(h1,h2):
            x = ListNode(0)
            temp = x
            while h1 and h2:
                if h1.val>h2.val:
                    x.next = h2
                    h2 = h2.next
                    x = x.next
                else:
                    x.next = h1
                    h1 = h1.next
                    x = x.next

            if h1:
                x.next = h1
                while x.next:
                    x = x.next
            elif h2:
                x.next = h2
                while x.next:
                    x= x.next
            return temp.next
        h1,h2 = breeak(head)
        h1,h2 = self.sortList(h1) ,self.sortList(h2)
        return merge(h1,h2)
        
        
