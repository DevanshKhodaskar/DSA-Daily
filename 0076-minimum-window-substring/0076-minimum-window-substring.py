class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dic = {}
        for ch in t:
            t_dic[ch] = 1 + t_dic.get(ch, 0)

        s_dic = {}
        l = 0
        ans = ""
        min_len = float('inf')

        for r in range(len(s)):
            if s[r] in t_dic:
                s_dic[s[r]] = s_dic.get(s[r], 0) + 1

            while all(s_dic.get(c, 0) >= t_dic[c] for c in t_dic):
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    ans = s[l:r+1]

                if s[l] in s_dic:
                    s_dic[s[l]] -= 1
                l += 1

        return ans
