class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                ans = i
                break

        return nums[ans]