class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        obs = set()
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obs.add((i,j))
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = {}
        memo[(m-1,n-1)]=1
        def helper(i,j):
            if (i,j) in obs:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            else:
                
                left = helper(i+1,j) if i+1<m else 0
                right = helper(i,j+1) if j+1<n else 0
                memo[(i,j)] = left+right
                return memo[(i,j)] 
        return helper(0,0)
            
            
        
            
            
        helper(0,0)
        return count