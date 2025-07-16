class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0 
        high = len(nums) - 1
        a = [-1,-1]

        if len(nums) == 0:
            return a

        while low<high and nums[low]!=target:
            low+=1
        if nums[low] == target:
            a[0] = low

        while low<high and nums[high]!=target:
            high-=1
        if nums[high] == target:
            a[1] = high

        return a
            