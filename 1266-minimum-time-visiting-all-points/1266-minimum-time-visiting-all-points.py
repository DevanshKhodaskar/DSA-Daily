class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(len(points) - 1):
            a = points[i][0]
            b = points[i][1]

            c = points[i+1][0]
            d = points[i+1][1]

            temp = max(abs(a-c),abs(b-d))
            ans+=temp

        return ans


        