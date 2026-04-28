class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                arr.append(grid[i][j])
        
        mod = arr[0] % x
        for i in arr:
            if i % x != mod:
                return -1
        
        arr.sort()
        mid = arr[len(arr)//2]
        
        ans = 0
        for i in arr:
            ans += abs(i - mid) // x
        
        return ans