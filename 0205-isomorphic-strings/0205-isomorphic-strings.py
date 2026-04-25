class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        a = set()

        for i in range(len(s)):
            if s[i] not in dic and t[i] not in a:   
                dic[s[i]] = t[i]
                a.add(t[i])


        for i in range(len(s)):
            if not s[i] in dic or dic[s[i]] != t[i]:
                return False
        return True 

        