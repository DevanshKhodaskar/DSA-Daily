class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = deque()
        result = []
        for i in range(len(nums)):
            while heap and heap[0] <= i-k:
                heap.popleft()

            while heap and nums[heap[-1]] < nums[i]:
                heap.pop()

            heap.append(i)




            if i>= k -1:
                result.append(nums[heap[0]])

        return result