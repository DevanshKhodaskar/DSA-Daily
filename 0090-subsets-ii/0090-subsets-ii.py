class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_ans = []
        
        def helper(nums, ans, final_ans, i):
            if i >= len(nums):
                final_ans.append(ans.copy())
                return
            ans.append(nums[i])
            helper(nums, ans, final_ans, i + 1)
            ans.pop()
            while i+1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(nums, ans, final_ans, i + 1)
        
        helper(nums, [], final_ans, 0)
        return final_ans