import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        t = 0
        if len(grid) == 1 or len(grid) == 0:
            return 0
        visited = set()
        visited.add((0, 0))

        arr = [[grid[0][0], 0, 0]]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]


        while arr:
            t += 1

            while arr and arr[0][0] <= t:
                val, x, y = heapq.heappop(arr)
                for i, j in directions:
                    xi = x + i
                    xj = y + j

                    if xi == n - 1 and xj == n - 1:
                        return max(t,grid[xi][xj])

                    if 0 <= xi < n and 0 <= xj < n and (xi, xj) not in visited:
                        visited.add((xi, xj))
                        heapq.heappush(arr, [grid[xi][xj], xi, xj])

                        
        return -1
