class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        memo = {}

        memo[(0,0)] = grid[0][0]
        def helper(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
        
            else:
                left = helper(i-1,j) if i>0 else float("inf")
                right = helper(i,j-1)if j>0 else float("inf")

                memo[(i,j)] = min(left,right)+grid[i][j]
                return memo[(i,j)]
        return helper(m-1,n-1)