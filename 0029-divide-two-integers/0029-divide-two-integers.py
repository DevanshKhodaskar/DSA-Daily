class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1


        negative = False
        Sum = 0
        negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        

        def helper(divisor , remainder):
            nonlocal Sum
            if remainder < divisor:
                return 
            else:
                i = 0
                while remainder >= divisor<<i:
                    i+=1
                i-=1
                Sum = Sum+ (1<<i)
            helper(divisor,(remainder - (divisor<<i)))
            return

        helper(divisor,dividend)
        if negative  == True:
            return -1*Sum

        return Sum

         