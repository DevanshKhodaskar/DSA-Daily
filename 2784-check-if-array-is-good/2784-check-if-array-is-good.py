class Solution:
    def isGood(self, nums: List[int]) -> bool:
    
        n = len(nums)
        if n ==0 or n ==1:
            return False
        nums.sort()
        for i in range(n-1):
            if nums[i] != i+1:
                return False
        if nums[n-1] !=nums[n-2]:
            return False
        return True
        
        