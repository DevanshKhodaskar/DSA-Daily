class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def helper(nums,k):
            l,r,total,ans = 0,0,0,0

            for r in range(len(nums)):
                total += 0 if nums[r]%2==0 else 1

                while total>k and l<=r:
                    total-=0 if nums[l]%2==0 else 1
                    l+=1

                ans+=r-l+1

            return ans
        

        return helper(nums,k) - helper(nums,k-1)