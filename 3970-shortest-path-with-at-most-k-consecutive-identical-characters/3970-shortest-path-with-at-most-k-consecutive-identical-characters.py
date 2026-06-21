from typing import List
import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        m = defaultdict(list)

        for u, v, c in edges:
            m[u].append((v, c))

        heap = []
        heapq.heappush(heap, (0, 0, 1))  

        dist = {(0, 1): 0}

        while heap:
            ci, vi, label = heapq.heappop(heap)

            if ci > dist.get((vi, label), float("inf")):
                continue

            if vi == n - 1:
                return ci

            for vj, cj in m[vi]:

                if labels[vi] == labels[vj]:
                    newLabel = label + 1

                    if newLabel > k:
                        continue
                else:
                    newLabel = 1

                newCost = ci + cj

                if newCost < dist.get((vj, newLabel), float("inf")):
                    dist[(vj, newLabel)] = newCost
                    heapq.heappush(heap, (newCost, vj, newLabel))

        return -1