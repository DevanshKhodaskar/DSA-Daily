class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        dp  = {}
        def solve(i,j):
            if i>=j:
                return 0
            else:
                if (i,j) in dp:
                    return dp[(i,j)]
                ans = float("inf")
                for k in range(i,j+1):
                    ans = min(ans,k+max(solve(i,k-1),solve(k+1,j)))
                    dp[(i,j)] = ans

                return dp[(i,j)]
        return solve(1,n)