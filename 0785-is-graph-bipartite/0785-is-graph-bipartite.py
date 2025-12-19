class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color = [-1] * len(graph)

        for i in range(len(graph)):
            if color[i] != -1:
                continue

            else:
                q = deque()
                q.append(i)

                color[i] = 0

                while q:
                    a = q.popleft()

                    arr = graph[a]

                    for j in arr:
                        if color[j] == color[a]:
                            return False
                        elif color[j] == -1:
                           color[j] = 1-color[a]
                           q.append(j)

        return True