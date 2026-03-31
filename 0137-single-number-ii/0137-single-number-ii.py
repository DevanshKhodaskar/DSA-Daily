class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if i in a:

                a[i]+=1
                if a[i] == 3:
                    a.pop(i)
            else:
                a[i] = 1
        for i in a:
            return i



        