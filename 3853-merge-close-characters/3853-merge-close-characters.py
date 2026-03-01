class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        result = []
        window = {}
        ans = []

        for i in s:
            if i in window and  window[i]>0:
                continue
            else:
                result.append(i)
                if i in window:
                    window[i]+=1
                else:
                    window[i] = 1
                ans.append(i)

                if len(result)>k:
                    rem_char = result[-k-1]
                    window[rem_char]-=1

        return "".join(ans)