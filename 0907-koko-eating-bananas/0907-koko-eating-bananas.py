import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def helper(piles,hr):
            ans = 0
            for i in piles:
                ans+=math.ceil(i/hr)

            return ans
        maxx = max(piles)
        l = 1
        r = maxx

        while l<r:
            mid = (l+r)//2

            temp = helper(piles,mid)
            if helper(piles, mid) > h:
                l = mid + 1
            else:
                r = mid

        return l

        
