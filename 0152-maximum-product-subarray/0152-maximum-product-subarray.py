class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minsum = maxsum  = 1
        ans = max(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                minsum = 1
                maxsum = 1
                continue
            else:
                temp = maxsum * nums[i]
                maxsum = max(temp , minsum* nums[i],nums[i])
                minsum = min(temp,minsum*nums[i] , nums[i])

            ans  = max(ans,maxsum)
        return ans