from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(i, arr):
            if len(arr) == k:
                ans.append(arr[:])  
                return
            
            if i > n:
                return

            arr.append(i)
            helper(i + 1, arr)

            arr.pop()
            helper(i + 1, arr)

        helper(1, [])
        return ans