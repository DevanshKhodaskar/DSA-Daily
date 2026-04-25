class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        nums = []

        for x, y in points:
            if y == 0:
                nums.append(x)
            elif x == side:
                nums.append(side + y)
            elif y == side:
                nums.append(3 * side - x)
            else:
                nums.append(4 * side - y)

        nums.sort()
        nums_ext = nums + [x + 4 * side for x in nums]

        def helper(n : int) -> bool:
            idx = [0] * k
            curr = nums[0]
            for i in range(1, k):
                j = bisect_left(nums, curr + n)
                if j == len(nums):
                    return False
                idx[i] = j
                curr = nums[j]
            if curr - nums[0] <= side * 4 - n:
                return True
            
            for idx[0] in range(1, idx[1]):
                for j in range(1, k):
                    while nums[idx[j]] < nums[idx[j - 1]] + n:
                        idx[j] += 1
                        if idx[j] == len(nums):
                            return False
                if nums[idx[-1]] - nums[idx[0]] <= side * 4 - n:
                    return True
            return False

        l, r = 0, 4 * side

        while l <= r:
            mid = (l + r) // 2
            if helper(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r