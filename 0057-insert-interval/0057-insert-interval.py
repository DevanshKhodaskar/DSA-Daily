from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        l, r = newInterval
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < l:
            ans.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= r:
            l = min(l, intervals[i][0])
            r = max(r, intervals[i][1])
            i += 1
        ans.append([l, r])

        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans
