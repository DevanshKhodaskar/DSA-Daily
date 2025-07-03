class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            a = int(digits[i])
            
            a = a+carry
            if carry == 1:
                carry = 0
            if a >= 10:
                a = a-10
                carry = 1

            digits[i] = a


        if carry == 1:
            digits = [1]+digits
        return digits