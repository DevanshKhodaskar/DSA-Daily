from collections import defaultdict
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        stickCount = []

        for i ,s in enumerate(stickers):
            stickCount.append(defaultdict(int))
            for c in s:
                stickCount[i][c]+=1

        for j in target:
            notFound = True
            for i in range(len(stickCount)):
                if j in stickCount[i]:
                    notFound = False
                    break
            if notFound:
                return -1
        
        memo = {}
        def helper(targ):
            if targ == "":
                return 0
            if targ in memo:
                return memo[targ]
            
            ans = float("inf")
            for i in range(len(stickCount)):
                temp = targ
                arr = stickCount[i].copy()

                if targ[0] in arr:
                    k =0
                    while k<len(temp):
                        if temp and temp[k] in arr and arr[temp[k]]>0:
                            arr[temp[k]]-=1
                            temp = temp[:k] + temp[k+1:]
                        else:
                            k+=1
                    ans = min(ans,helper(temp)+1)
            memo[targ] = ans
            return memo[targ]
        return helper(target )



