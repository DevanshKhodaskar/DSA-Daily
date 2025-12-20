class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack = []
        ans = []
        dependency = []
        for _ in range(numCourses):
            dependency.append([])

        for a,b in prerequisites:
            dependency[b].append(a)

            


        cycle = False
        visited = [0] * numCourses

        def dfs(visited,stack,cur):
            nonlocal cycle
            if visited[cur] == 2:
                return
            if visited[cur] == 1:
                cycle = True
                return 

            visited[cur] = 1
            for i in dependency[cur]:
                dfs(visited,stack,i)
            visited[cur] = 2
            stack.append(cur)
            

        
        for i in range(numCourses):
            if visited[i] == 0:
                dfs(visited,stack,i)
        if cycle:
            return []
        while stack:
            ans.append(stack.pop())

        return ans
                


            

        