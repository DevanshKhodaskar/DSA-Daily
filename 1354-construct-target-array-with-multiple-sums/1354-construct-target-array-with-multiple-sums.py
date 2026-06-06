import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        a = [-x for x in target]
        heapq.heapify(a)

        summ = sum(target)


        while (-a[0]) > 1:
            ele = -heapq.heappop(a)
            rest = summ-ele
            if rest == 0 or ele<rest:
                return False

            ele =  ele%rest
            if ele == 0:
                return rest == 1
            summ = rest+ele
            heapq.heappush(a,-ele)

        return True