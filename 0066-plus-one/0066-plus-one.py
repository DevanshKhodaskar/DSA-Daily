class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            c = digits[i]+carry

            if c < 10:
                digits[i] = c
                carry = 0
                return digits
            else:
                carry = 1
                
                digits[i] = c%10
        if carry == 1:
            digits = [1]+digits

        return digits


        