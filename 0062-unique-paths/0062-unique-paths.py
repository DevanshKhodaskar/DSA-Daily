class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        memo = {}
        memo[(m-1,n-1)]=1
        def helper(i,j):

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