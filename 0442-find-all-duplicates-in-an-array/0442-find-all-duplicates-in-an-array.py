class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = set()
        ans = []
        for i in nums:
            if i in a:
                ans.append(i)
            else:
                a.add(i)
        return ans