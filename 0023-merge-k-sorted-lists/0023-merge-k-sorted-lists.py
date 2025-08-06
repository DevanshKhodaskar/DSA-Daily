# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == [] or lists == None:
            return None
        pq = []
        for i in range(len(lists)):
            if lists[i] != None:
                item = (lists[i].val,i,lists[i])
                hq.heappush(pq,item)

        d = ListNode(0)
        ans = d

        while pq != []:
            heap_item = hq.heappop(pq)
            ans.next = heap_item[2]
            ans = ans.next
            if heap_item[2].next != None:        
                item = (heap_item[2].next.val, heap_item[1], heap_item[2].next)
                heapq.heappush(pq, item)

        return d.next
