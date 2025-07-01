class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        a = -1
        b = -1
        c = -1
        ans = 0

        for i in range(len(s)):
            if s[i] == 'a':
                a = i
            elif s[i] == 'b':
                b = i
            else:
                c = i

            #print(f"a:{a}\tb:{b}\tc:{c}")
            if a !=-1 and b !=-1 and c != -1:
                temp = min(a,b,c)

                ans+=temp+1

        return ans
