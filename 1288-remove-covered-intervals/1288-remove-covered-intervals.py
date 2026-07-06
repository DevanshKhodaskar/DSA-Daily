class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        i = 0  
        count = 0
        while i <len(intervals):
            j = i+1

            while j<len(intervals) and intervals[j][1] <= intervals[i][1]:
                j+=1
            i = j
            count+=1
        return count

        

