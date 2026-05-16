class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        def helper(x):
            temp = x

            for actual, minimum in tasks:
                if temp < minimum:
                    return False

                temp -= actual

            return True

        l = max(m for a, m in tasks)
        r = sum(m for a, m in tasks)

        while l < r:
            mid = (l + r) // 2

            if helper(mid):
                r = mid
            else:
                l = mid + 1

        return l