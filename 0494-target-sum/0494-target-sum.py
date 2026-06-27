class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        memo = {}
        def helper(summ,i):
            if (summ,i) in memo:
                return memo[(summ,i)]
            if i == len(nums):
                if summ == target:
                    memo[(summ,i)] = 1
                    return memo[(summ,i)]
                else:
                    memo[(summ,i)] = 0
                    return memo[(summ,i)]
            
            
            else:
                left = helper(summ+nums[i],i+1)
                right = helper(summ-nums[i],i+1)
                memo[(summ,i)] = left+right
                return memo[(summ,i)]

        return helper(0,0)

            