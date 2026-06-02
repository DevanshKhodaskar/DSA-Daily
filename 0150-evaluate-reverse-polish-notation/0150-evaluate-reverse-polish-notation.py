class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ["+","/","*","-"]
        def helper(arr):
            opr = arr.pop()

            if opr in operations:
                left = helper(arr)
                right = helper(arr)
                temp =str( "("+right+opr+left+")")
                return str(int(eval(temp)))
            else:
                return"("+ opr+")"
        ans = helper(tokens)
        return int(eval(ans))
                
