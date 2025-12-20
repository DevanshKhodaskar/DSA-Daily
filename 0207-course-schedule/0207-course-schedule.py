from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            dependency[b].append(a)

        visited = [0] * numCourses   
        cycle  =False

        def dfs(cur):
            nonlocal cycle

            if visited[cur] == 1:
                cycle = True
                return
            if visited[cur] == 2:
                return

            visited[cur] = 1
            for i in dependency[cur]:
                dfs(i)
            visited[cur] = 2

        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)

        return not cycle
