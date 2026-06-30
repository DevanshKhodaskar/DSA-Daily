class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = {
            'a':-1,
            'b':-1,
            'c':-1,
        }
        count = 0
        for j in range(len(s)):
            dic[s[j]] = j
            minele = min(dic,key = lambda k:dic[k])
            if dic[minele] == -1:
                continue
            else:
                count+=dic[minele]+1

        return count
       