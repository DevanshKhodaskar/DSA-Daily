class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}

        def solve(n, alice):
            if n == 0:
                return not alice

            elif (n, alice) in memo:
                return memo[(n, alice)]

            else:
                i = 1

                while i * i <= n:

                    if alice == True:
                        if solve(n - i * i, not alice) == True:
                            memo[(n, alice)] = True
                            return memo[(n, alice)]

                    else:
                        if solve(n - i * i, not alice) == False:
                            memo[(n, alice)] = False
                            return memo[(n, alice)]

                    i += 1

                memo[(n, alice)] = not alice
                return memo[(n, alice)]

        return solve(n, True)