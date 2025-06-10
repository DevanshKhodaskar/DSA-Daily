class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        prime_list = [True]*n
        prime_list[0] = prime_list[1] = False
        count=0
        for i in range(2,n):
            if prime_list[i]:
                # print(f"index:{i}")
                count+=1
                temp = i
                for j in range(i*i,n,i):
                    # print(f"for index:{i} falsed value is {j}")
                    prime_list[j] = False
        # print(prime_list)
        return count





        