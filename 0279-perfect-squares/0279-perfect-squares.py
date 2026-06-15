import math
class Solution:

    def numSquares(self, n: int) -> int:
        i = 1
        memo={}
        while i*i<n:
            memo[i] = i*i
            i+=1

        def helper(n):
            x = math.floor(sqrt(n))
            if x*x  == n:
                return 1
            if n in memo:
                return memo[n] 
            
            else:
                ans = n
                for i in range(x,0,-1):
                    temp = 1+helper(n-i*i)
                    ans = min(temp,ans)
                memo[n] = ans
                return memo[n]

        return helper(n)
            
        