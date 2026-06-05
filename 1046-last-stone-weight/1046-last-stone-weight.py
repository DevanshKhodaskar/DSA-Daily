import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) >1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            heapq.heappush(stones,(a-b))
        return abs(stones[0])