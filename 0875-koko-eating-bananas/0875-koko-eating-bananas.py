import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def helper(n):
            total = 0
            for i in range(len(piles)):
                total+=math.ceil(piles[i]/ n)

            return total<=h

        l = 1
        r = max(piles)

        while l<=r:
            mid = (l+r)//2

            if helper(mid):
                r = mid-1
            else:
                l = mid+1
        return l