class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 0 and len(nums) == 1:
            return True
        first = nums[0]
        last = nums[-1]
        flag = False
        temp = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if flag:
                    return False
                flag  = True

        if flag and last > first:
            return False

        return True
