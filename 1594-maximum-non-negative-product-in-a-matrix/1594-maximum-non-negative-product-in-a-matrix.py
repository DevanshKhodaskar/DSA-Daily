class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp_min  = [[0]*m for _ in range(n)]
        dp_max  = [[0]*m for _ in range(n)]


        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        for j in range(1,m):
              dp_min[0][j] = dp_max[0][j] = grid[0][j]*dp_max[0][j-1]
        
        for i in range(1,n):
            dp_min[i][0] = dp_max[i][0] = grid[i][0]*dp_min[i-1][0]

        for i in range(1,n):
            for j in range(1,m):
                val = grid[i][j]

                arr = [
                    dp_max[i-1][j]*val,
                    dp_max[i][j-1]*val,
                    dp_min[i-1][j]*val,
                    dp_min[i][j-1]*val,
                       
                ]
                dp_min[i][j] = min(arr)
                dp_max[i][j] = max(arr)
        
        ans = dp_max[n-1][m-1] 

        mod = 10**9 +7

        if ans>=0:
            return ans%mod
        
        return -1
