class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def helper(nums,k):
            l = 0
            temp_ans = 0
            r = 0
            d = {}
            while r <= len(nums)-1:

                d[nums[r]] = d.get(nums[r], 0) + 1

            

                while len(d)>k:
                    d[nums[l]] = d[nums[l]] - 1
                    if d[nums[l]] == 0:
                        d.pop(nums[l])
                    l+=1
                temp_ans+=r-l+1
                r+=1
            return temp_ans
                
        return helper(nums,k) - helper(nums,k-1)
                    
            

        