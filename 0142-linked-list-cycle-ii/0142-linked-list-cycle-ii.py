class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = {}

        ptr = head

        while ptr is not None:
            if ptr in visited:
                return ptr  

            visited[ptr] = True
            ptr = ptr.next

        return None  
