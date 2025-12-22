class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        newSet=[float("+inf")] *n
        newSet[k-1] = 0

        tempSet = newSet.copy()
        for i in range(n):
            newSet = tempSet.copy()
            for s,d,c in times:
                
                tempSet[d-1] = min(tempSet[d-1],newSet[s-1]+c)
            newSet = tempSet.copy()

        ans = max(newSet)
        return ans if ans != float("+inf") else -1



        