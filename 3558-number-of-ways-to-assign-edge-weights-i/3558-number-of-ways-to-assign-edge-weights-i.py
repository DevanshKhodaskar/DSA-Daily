from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        m = defaultdict(list)

        for i, j in edges:
            m[i].append(j)
            m[j].append(i)

        count = 0
        q = deque([1])
        visited = {1}

        while q:
            temp = []
            while q:
                a = q.popleft()
                for nxt in m[a]:
                    if nxt not in visited:
                        visited.add(nxt)
                        temp.append(nxt)
            q.extend(temp)
            count += 1

        k = count - 1
        return pow(2, k - 1, MOD)