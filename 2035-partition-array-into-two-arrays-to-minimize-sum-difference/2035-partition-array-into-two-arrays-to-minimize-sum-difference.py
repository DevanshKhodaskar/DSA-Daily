from collections import defaultdict
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        half = n//2
        total = sum(nums)
        target = total//2

        left = nums[:half]
        right = nums[half:]
        lsum = defaultdict(set)
        rsum = defaultdict(set)

        for mask in range(1 << half):
            lcs = 0
            count = 0
            rcs = 0

            for i in range(half):
                if mask & (1 << i):
                    lcs += left[i]
                    count += 1
                    rcs+=right[i]

            lsum[count].add(lcs)
            rsum[count].add(rcs)
        ans = float("inf")

        for k in range(half + 1):
            left_sums = sorted(lsum[k])
            right_sums = sorted(rsum[half - k])

            i = 0
            j = len(right_sums) - 1

            while i < len(left_sums) and j >= 0:
                curr = left_sums[i] + right_sums[j]

                ans = min(ans, abs(total - 2 * curr))

                if curr > total / 2:
                    j -= 1
                else:
                    i += 1

        return ans