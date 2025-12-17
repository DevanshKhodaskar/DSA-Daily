from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList :
            return 0
        wordset = set()
        for i in wordList:
            wordset.add(i)

        stack = deque()
        stack.append((beginWord,1))
        


        def helper(word,n):

            for i in range(len(word)):

                for j in range(ord('a'), ord('z') + 1):
                    newWord =  word[:i]+chr(j)+word[i+1:]  
                    if newWord in wordset:
                        wordset.remove(newWord)
                        stack.append((newWord,n))




        while stack:
            a,b = stack.popleft()
            if a == endWord:
                return b
            else:
                helper(a,b+1)


        return 0





