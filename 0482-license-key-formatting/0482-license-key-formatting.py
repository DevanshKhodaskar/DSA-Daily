class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        arr = s.split("-")
        temp = "".join(arr)
        temp = temp.upper()
        for i in range(len(temp)-k,0,-k):
            temp = temp[:i]+"-"+temp[i:]
        return temp