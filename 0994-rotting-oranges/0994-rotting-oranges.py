from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        a = len(grid)
        b = len(grid[0])
        ans = 0
        q = deque()
        for i in range(a):
            for j in range(b):
                if grid[i][j] == 2:
                    q.append((i,j,0))



        while q:
            i,j,t = q.popleft()
            ans = max(t,ans)


            if i + 1 < a and grid[i + 1][j] == 1:
                grid[i + 1][j] = 2
                q.append((i + 1, j, t + 1))

            if i - 1 >= 0 and grid[i - 1][j] == 1:
                grid[i - 1][j] = 2
                q.append((i - 1, j, t + 1))

            if j + 1 < b and grid[i][j + 1] == 1:
                grid[i][j + 1] = 2
                q.append((i, j + 1, t + 1))

            if j - 1 >= 0 and grid[i][j - 1] == 1:
                grid[i][j - 1] = 2
                q.append((i, j - 1, t + 1))


        for i in range(a):
            for j in range(b):
                if grid[i][j] == 1:
                    return -1
        return ans

        