class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        table  = {}
        m = float("inf")
        for i in nums:
            if i>0:
                table[i] = i+1
                m = min(m,i)
        if m>1:
            # print(temp)
            return 1
        while m in table:
            m = table[m]

        return m
            