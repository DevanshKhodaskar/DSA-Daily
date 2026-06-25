class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        while idx <= len(self.bit) - 1:
            self.bit[idx] += val
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        offset = n + 2
        size = 2 * n + 5

        bit = Fenwick(size)

        prefix = 0
        ans = 0

        bit.update(offset, 1)

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            idx = prefix + offset

            ans += bit.query(idx - 1)

            bit.update(idx, 1)

        return ans