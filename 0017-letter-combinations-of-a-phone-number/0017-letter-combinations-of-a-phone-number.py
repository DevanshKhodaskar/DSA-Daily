class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        keypad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def helper(keypad,final_ans,ans,digits,i):
            if i == len(digits):
                final_ans.append(ans[:])
                return

            for j in keypad[digits[i]]:
                
                ans = ans+str(j)
                helper(keypad,final_ans,ans,digits,i+1)
                ans = ans[:len(ans)-1]


        final_ans = []

        helper(keypad,final_ans,"",digits,0)
        for i in final_ans:
            if i == "":
                final_ans.remove(i)
        return final_ans