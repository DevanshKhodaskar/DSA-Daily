import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0] / h)

        minspeed = 1
        maxspeed = max(piles)

        while minspeed<maxspeed:
            mid = (minspeed+maxspeed)//2
            temp = 0
            for i in piles:
                temp +=math.ceil(i/mid)

          
            if temp>h:
                minspeed=mid+1
            else:
                maxspeed=mid

        return minspeed

        
        
