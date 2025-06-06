class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def helper(line, wordDict,used):
            if line == "":
                return True
            if line in used:
                return used[line]

            for i in range(1, len(line) + 1): 
                if line[:i] in wordDict:
                    if helper(line[i:], wordDict,used): 
                        used[line] = True
                        return True
            used[line] = False
            return False
        
        used = {}
        return helper(s, wordDict,used)