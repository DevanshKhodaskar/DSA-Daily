class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        ans = []

        def dfs(i):
            stack = [i]
            while stack:
                ele = stack.pop()
                visited.add(ele)
                for j in range(len(isConnected[i])):
                    if isConnected[ele][j] == 1 and j not in visited :stack.append(j)



        for i in range(len(isConnected)):
            if i not in visited:
                ans.append(i)
                dfs(i)
        print(ans)
        return len(ans)