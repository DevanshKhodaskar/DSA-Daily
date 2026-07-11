from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        nighbour = defaultdict(list)

        for u, v in edges:
            nighbour[u].append(v)
            nighbour[v].append(u)

        visited = set()

        def helper(node):
            q = deque([node])
            visited.add(node)

            component = []

            while q:
                ele = q.popleft()
                component.append(ele)

                for ne in nighbour[ele]:
                    if ne not in visited:      
                        visited.add(ne)        
                        q.append(ne)

            k = len(component)

            for node in component:
                if len(nighbour[node]) != k - 1:
                    return False

            return True

        ans = 0

        for i in range(n):
            if i not in visited:
                if helper(i):
                    ans += 1

        return ans