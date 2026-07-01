class Solution:
    def minDays(self, n: int) -> int:
        dp = {}
     
        dp[1] = 1
        dp[0] = 0
        

        def helper(n):
            if n in dp:
                return dp[n]
            else:

                ans = float("inf")        
                ans = min(ans ,n%2+1+ helper(n//2))
                ans = min(ans ,n%3+1+ helper(n//3))
                dp[n] = ans
                return dp[n]
        return helper(n)
