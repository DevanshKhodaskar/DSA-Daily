class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        for j in range(len(triangle[-1])):
            memo[(len(triangle)-1),j] = triangle[(len(triangle)-1)][j]
        def helper(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            else:
                left = helper(i+1,j) if i<len(triangle)-1 else float("inf")
                right = helper(i+1,j+1) if  i<len(triangle)-1 and j<len(triangle[i]) else float("inf")
                
                memo[(i,j)] = min(left,right)+triangle[i][j]
                return memo[(i,j)]
        return helper(0,0)