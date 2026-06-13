class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""

        for word in words:
            summ = 0
            for ch in word:
                summ += weights[ord(ch) - 97]
            ans += chr(ord('z') - (summ % 26))

        return ans