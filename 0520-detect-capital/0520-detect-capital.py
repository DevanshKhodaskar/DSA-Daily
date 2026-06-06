class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<2:
            return True
        allLower = False
        allUpper = False
        initial = False
        if word[0].islower():
            allLower= True
        elif word[0].isupper() and word[1].isupper():
            allUpper = True
        else:
            initial = True
        
        # print(f"{allLower}\t{allUpper}\t{initial}")
        if allLower:
            for  i in word:
                if i.isupper():
                    return False
        elif allUpper:
            for i in word:
                if i.islower():
                    return False
        else:
            for i in range(1,len(word)):
                if word[i].isupper():
                    return False
        return True