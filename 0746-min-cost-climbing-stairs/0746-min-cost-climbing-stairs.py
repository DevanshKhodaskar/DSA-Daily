class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        memo[0] = 0
        memo[1] = 0

        def helper(n):
            if n in memo:
                return memo[n]

            else:

                left = helper(n-1)+cost[n-1]
                right = helper(n-2)+cost[n-2]
                memo[n] = min(left,right)
                return memo[n]
        return helper(len(cost))