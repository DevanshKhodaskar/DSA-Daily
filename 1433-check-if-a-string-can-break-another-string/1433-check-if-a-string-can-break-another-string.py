class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        S1 = []
        S2 = []
        for x in s1:
            S1.append(x) 
        S1.sort()
        for x in s2:
            S2.append(x) 
        S1.sort()
        S2.sort()

        def helper(s1 ,s2):
            for i in range(len(s1)):
                if s1[i]>s2[i]:
                    return False
            return True

        return helper(S1,S2) or helper(S2,S1)