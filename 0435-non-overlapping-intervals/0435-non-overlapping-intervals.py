class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        a = list(set(map(tuple, intervals)))
        a = [list(t) for t in a]
        a.sort(key = lambda x:x[1])
        counter = len(intervals) - len(a)
        prev = float('-inf')
        for l,r in a:
            if l>=prev:
                prev = r 

            else:
                counter+=1 

        return counter

