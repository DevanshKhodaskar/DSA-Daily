class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def helper(n):
            if n == 1:
                return [1]

            odd = [2 * x - 1 for x in helper((n + 1) // 2)]
            even = [2 * x for x in helper(n // 2)]

            return odd + even

        return helper(n)