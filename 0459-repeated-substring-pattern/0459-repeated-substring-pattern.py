class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp = ""
        left = 0
        right = 0
        n = len(s)


        def helper(temp):
            x = 0
            if len(temp) == 0:
                return False
            for i in range(len(temp),n+1,len(temp)):
                if s[x:i] != temp:
                    return False
                x = i
            return True and i == n


        while  right < n and right+1<n:
            left+=1
            right+=2

            if s[:left] == s[left:right]:
                temp = s[:left]
                if helper(temp):
                    return True

        return False
                
                
                
        