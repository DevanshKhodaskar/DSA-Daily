class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = float("-inf")
        summ = 0
        for i in nums:
            summ+=i
            max_val = max(summ,max_val)

            if summ<=0:
                summ =0
        return max_val
        