import heapq
from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        n = len(grid)
        grid2 = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid2[i][j] = 0
                    q.append((i, j))

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        while q:
            i, j = q.popleft()

            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                if 0 <= ni < n and 0 <= nj < n and grid2[ni][nj] == -1:
                    grid2[ni][nj] = grid2[i][j] + 1
                    q.append((ni, nj))

        visited = set((0,0))
        heap = [(-grid2[0][0] , 0 ,0)]
        heapq.heapify(heap)
        ans = 0
        while  heap :
            val , i , j = heapq.heappop(heap)
            
            if i == n-1 and j == n-1:
                return -val
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for x ,y in directions:
                ni,nj = i+x , j+y

                if 0<=ni<n and 0<=nj<n and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    temp = min(-val , grid2[ni][nj])
                    heapq.heappush(heap,(-temp,ni,nj))
        return -1




