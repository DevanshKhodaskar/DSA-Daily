class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = bin(start)[2:]
        b = bin(goal)[2:]

        if len(a)> len(b):
            b = "0"*(len(a)-len(b)) + b

        if len(a)< len(b):
            a = "0"*(len(b)-len(a)) + a
        
        count = 0
        print(f"a:{a}  b:{b}")
        for i in range(len(a)):
            if a[i] != b[i]:
                count+=1


        return count       