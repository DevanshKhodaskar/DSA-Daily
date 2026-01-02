class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        i = 0
        while i <len(nums):
            if nums[i] == 0:
                nums[:] = nums[:i]+nums[i+1:]
                count+=1
            else:i+=1
        nums+=[0 for i in range(count)]
            

        