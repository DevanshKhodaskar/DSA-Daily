import math
class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        memo[1] =1
        memo[0] = 1

        def helper(no):
            if no in memo:
                return memo[no]
            else:
                ans = 0
                for i in range(1,no+1):
                    left =helper(i-1)
                    right = helper(no-i)
                    ans+=left*right

                memo[no] =  ans
                return memo[no]
        return helper(n)