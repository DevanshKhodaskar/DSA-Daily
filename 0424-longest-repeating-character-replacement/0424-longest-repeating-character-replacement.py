class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = {}
        max_count = 0
        l = 0
        ans = 0

        for i in range(len(s)):
            if s[i] in a:
                a[s[i]] += 1
            else:
                a[s[i]] = 1

            max_count = max(max_count, a[s[i]])

            if i - l + 1 - max_count > k:
                a[s[l]] -= 1
                l += 1

            ans = max(ans, i - l + 1)

        return ans
