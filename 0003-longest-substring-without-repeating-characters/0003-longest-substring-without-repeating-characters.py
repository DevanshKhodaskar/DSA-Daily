from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        arr = deque()

        dic = {}
        ans = 0
        for i in range(len(s)):
            if s[i] not in dic:
                arr.append(s[i])
                dic[s[i]] = 1
                ans = max(ans,len(arr))
            elif dic[s[i]] == 0:
                arr.append(s[i])
                dic[s[i]] = 1+dic[s[i]]
                ans = max(ans,len(arr))
            else:
                while dic[s[i]] != 0:
                    b = arr.popleft()
                    dic[b] = dic[b]-1
                arr.append(s[i])
                dic[s[i]] = 1+dic[s[i]]
                ans = max(ans,len(arr))
                
        return ans
            
            
    
    
            
        