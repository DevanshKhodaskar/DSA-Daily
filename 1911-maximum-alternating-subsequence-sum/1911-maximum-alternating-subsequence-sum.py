class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        

        memo = {}


        def helper(i,iseven):
            if i == len(nums):
                return 0
            if (i,iseven) in memo:
                return memo[(i,iseven)]
            else:
                total = nums[i] if iseven else -nums[i]
                memo[(i,iseven)] = max(total+helper(i+1,not iseven) ,helper(i+1,iseven))
                return memo[(i,iseven)]
        return helper(0,True)

