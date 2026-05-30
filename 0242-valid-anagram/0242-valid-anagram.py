from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = defaultdict(int)
        m2  = defaultdict(int)

        for i in s:
            m1[i] +=1
        for j in t:
            m2[j]+=1
        
        if len(m1)!=len(m2):
            return False
        
        for i in m1:
            if i not in m2:
                return False
            if m1[i]!=m2[i]:
                return False
        return True