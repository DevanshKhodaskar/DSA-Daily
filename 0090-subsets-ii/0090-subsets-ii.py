class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        nums.sort()
        n = len(nums)

        def helper(i, temp):

            if i == n:
                ans.add(tuple(temp))     
                return

            helper(i + 1, temp)

            temp.append(nums[i])

            helper(i + 1, temp)

            temp.pop()                  

        helper(0, [])

        return [list(x) for x in ans]   