class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()

        s.sort()
        counter= 0 
        i ,j = 0,0
        while i != len(s) and j != len(g):
            if s[i]>=g[j]:
                counter+=1
                i+=1
                j+=1

            else:
                i+=1

        return counter

        
        