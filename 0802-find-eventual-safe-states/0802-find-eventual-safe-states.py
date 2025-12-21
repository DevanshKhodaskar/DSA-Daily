class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = [False]*len(graph)
        visited = [False]*len(graph)

        for i in range(len(graph)):
            if graph[i] == []:
                safe[i] = True
                visited[i] = True

        def dfs(ele):

            if safe[ele]:
                return True
            if visited[ele]:
                return False

        
            visited[ele]=True
            flag = True
            for n in graph[ele]:
                flag = flag and dfs(n)
            if flag == True:
                safe[ele] = True
            return flag
        
        ans = []
        for i in range(len(graph)):
            if dfs(i) == True:
                ans.append(i)

        return ans
                




        