class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
    
        def helper(i) -> int:
            if i == n:
                return 1
            elif i > n:
                return 0
            else:
                if i in memo:
                    return memo[i]
                else:
                    left = helper(i+1)
                    right = helper(i+2)

                    memo[i] = left+right
                    return memo[i]
            
            return memo[n]


        return helper(0)