class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return min(nums)

        low  = 0
        high = len(nums) - 1
    
        mid = (low+high)//2

        if nums[low]<nums[mid]:
            if nums[low]<nums[high]:
                return nums[low]

            else:
                ans  = nums[mid] 
                for i in range(mid,high+1):
                    if nums[i]<ans:
                        ans = nums[i]
                return ans
        else:
            ans  = nums[mid] 
            for i in range(low,mid):
                if nums[i]<ans:
                    ans = nums[i]
            return ans


        