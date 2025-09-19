class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0 
        r = 0
        j = 0
        steps = 0
        while r<len(nums)-1:
            temp  = 0
            for i in range(l,r+1):
                temp = max(temp,nums[i]+i)
            
            steps += 1
            l = r+1
            r = temp

        return steps
            
        