from heapq import heappush,heappop
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        noofPaths = [0]*n
        shortPath = [float("+inf")]*n
        MOD = 10**9 + 7
        shortPath[0] = 0
        noofPaths[0] = 1
        graph = [[] for _ in range(n)]
        for s,d,c in roads:
            graph[s].append((d,c))
            graph[d].append((s,c))

        q = [(0,0)]
        
        while q:
            cost,node = heappop(q)

            if cost>shortPath[node]:
                continue
            
            else:
                for d,c in graph[node]:
                    newcost = cost+c

                    if newcost<shortPath[d]:
                        noofPaths[d] = noofPaths[node]
                        shortPath[d] = newcost
                        heappush(q,(newcost,d))
                    elif newcost == shortPath[d]:
                        noofPaths[d] = (noofPaths[d]+noofPaths[node])%MOD

        return noofPaths[-1]
        


        