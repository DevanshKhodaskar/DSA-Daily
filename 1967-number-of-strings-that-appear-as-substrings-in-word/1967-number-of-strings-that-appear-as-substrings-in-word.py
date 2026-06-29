class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        a = set()

        for i in range((len(word))):
            for j in range(i,len(word)+1):
                a.add(word[i:j])
        ans = 0
        for k in patterns:
            if k in a:
                ans+=1
        return ans