import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()

        low = 1
        high = max(nums)

        while low<high:
            mid = (low+high)//2
            t = self.possible(nums,threshold,mid)
            if t:
                high = mid
            else:
                low = mid + 1
        return low



    def possible(self,nums,threshold,key):
        summ = 0
        for i in nums:
            summ+=math.ceil(i/key)
        
        if summ <= threshold:
            return 1
        else:
            return 0
        
        