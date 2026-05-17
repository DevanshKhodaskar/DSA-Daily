from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        s = set()
        s.add(start)
        q = deque()
        q.append(start)
        n = len(arr)
        if arr[start] == 0:
            return True
        while q:
            a = q.popleft()
            left = a - arr[a]
            right = a + arr[a]
            if 0<=left<n:
                if arr[left] == 0:
                    return True
                else:
                    if left not in s:
                        q.append(left)
                        s.add(left)
            if 0<=right<n:
                if arr[right] == 0:
                    return True
                else:
                    if right not in s:
                        q.append(right)
                        s.add(right)
        return False