class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(nums,goal):
            l,r,total,ans= 0,0,0,0

            for r in range(len(nums)):
                total += nums[r]
                while total>goal and l<=r:
                    total-=nums[l]
                    l+=1

                ans+=r - l+1

            return ans



        return helper(nums,goal) - helper(nums,goal-1)

        