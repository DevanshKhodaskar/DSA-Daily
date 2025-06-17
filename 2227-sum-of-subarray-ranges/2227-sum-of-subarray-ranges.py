class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sub_max = 0
        sub_min = 0

        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1][1]:
                j, m = stack.pop()
                l = j - stack[-1][0] if stack else j + 1   
                r = i - j
                sub_min += l * r * m
            stack.append([i, nums[i]])

        while stack: 
            j, m = stack.pop()
            l = j - stack[-1][0] if stack else j + 1       
            r = len(nums) - j
            sub_min += l * r * m    

        stack2 = []
        for i in range(len(nums)):
            while stack2 and nums[i] > stack2[-1][1]:
                j, m = stack2.pop()
                l = j - stack2[-1][0] if stack2 else j + 1  
                r = i - j
                sub_max += l * r * m
            stack2.append([i, nums[i]])

        while stack2:  
            j, m = stack2.pop()
            l = j - stack2[-1][0] if stack2 else j + 1     
            r = len(nums) - j
            sub_max += l * r * m 

        return sub_max - sub_min
