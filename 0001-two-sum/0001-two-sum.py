class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = nums.copy()
            temp[i]='a'  
            print("Hello World")
            if (target-nums[i]) in temp:
                
                complement=temp.index(target-nums[i])
                print([i,complement])
                return [i,complement]
            