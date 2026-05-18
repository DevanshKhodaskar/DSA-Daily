class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(s):
            for i in range(len(s)//2):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True

        s  = s.split(" ")

        ans  = []
        for i in s:
            ans.append("".join(ch for ch in i if ch.isalpha() or ch.isdigit() )) 
        temp  = "".join(i for i in ans)
        temp =temp.lower()
        print(temp)
        return (helper(temp))

        
        