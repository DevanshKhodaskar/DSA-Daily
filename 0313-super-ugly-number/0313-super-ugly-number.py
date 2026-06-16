class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ptr = [0] * len(primes)
        ans = [1] * n

        for i in range(1, n):          
            temp2 = float("inf")

            for j in range(len(ptr)):
                if primes[j] * ans[ptr[j]] < temp2:
                    temp2 = primes[j] * ans[ptr[j]]

            ans[i] = temp2

            for j in range(len(ptr)):
                if primes[j] * ans[ptr[j]] == temp2:
                    ptr[j] += 1

        return ans[-1]