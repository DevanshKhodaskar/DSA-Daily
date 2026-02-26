class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(x):
            if x >=len(nums): 
                return 0

            elif x in memo:
                return memo[x]
            else:
                left =  nums[x]+helper(x+2)

                right = helper(x+1)

            memo[x] =  max(left , right)
            return memo[x]

        return helper(0)

        