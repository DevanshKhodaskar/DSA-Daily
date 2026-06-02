class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = set()
        twice = -1
        for i in nums:
            if i in a:
                twice = i
            a.add(i)
        for i in range(1,len(nums)+1):
            if i not in a:
                return [twice,i]