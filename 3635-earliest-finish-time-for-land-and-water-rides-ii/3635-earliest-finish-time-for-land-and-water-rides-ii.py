class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        totalLand = [landStartTime[x]+landDuration[x] for x in range(len(landDuration))]
        totalWater = [waterStartTime[x]+waterDuration[x] for x in range(len(waterDuration))]

        minLand = min(totalLand)
        minLandIndex = totalLand.index(minLand)
        ans = float("inf")
        for i in range(len(waterDuration)):
            if waterStartTime[i]>=minLand:
                ans = min(ans,minLand+waterDuration[i]+(waterStartTime[i]-minLand))
            else:
                ans = min(ans,minLand+waterDuration[i])

        minWater = min(totalWater)

        for j in range(len(landDuration)):
            if landStartTime[j]>=minWater:
                ans = min(ans,minWater+landDuration[j]+(landStartTime[j]-minWater))
            else:
                ans = min(ans,minWater+landDuration[j])
                
        return ans
     