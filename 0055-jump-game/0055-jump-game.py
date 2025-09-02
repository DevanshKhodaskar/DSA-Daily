class Solution:
    def canJump(self, nums: List[int]) -> bool:
        temp  = 1
        for i in range(len(nums)):
            temp -=1
            if temp<0:
                return False
            if nums[i] > temp:
                temp = nums[i]

        return True 

            


        