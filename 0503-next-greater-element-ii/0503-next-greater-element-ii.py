class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1]*len(nums)
        for i in range(len(nums)):
            if len(stack) == 0:
                stack.append(i)
            elif nums[i]<=nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums[stack[-1]] < nums[i]:
                    ans[stack.pop()] = nums[i]
                stack.append(i)


        for i in range(len(nums)):
            
            while stack and nums[stack[-1]]<nums[i]:
                
                ans[stack.pop()] = nums[i]
        
        return ans
