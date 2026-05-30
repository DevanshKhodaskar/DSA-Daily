class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 !=0:
            return False
        target = s//2
        memo = {}
        def helper(summ,i):
            if summ>target:
                return False

            if summ == target:
                return True
            if i == len(nums):
                return False
            if (summ,i) in memo:
                return memo[(summ,i)]



            memo[(summ,i)] =  helper(summ+nums[i]  ,i+1) or helper(summ,i+1)
            return memo[(summ,i)]
        return helper(0,0)

            