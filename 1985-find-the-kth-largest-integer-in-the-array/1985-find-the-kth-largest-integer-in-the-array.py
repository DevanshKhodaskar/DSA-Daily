import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int, nums))
        nums = [-x for x in nums]
        heapq.heapify(nums)
        ans = 0
        for i in range(k):
            ans = heapq.heappop(nums)
            print(ans)
        return str(-ans)