from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = deque(sandwiches)
        st = deque(students)
        flag = -1
        while s and st:
            if s[0] == st[0]:
                st.popleft()
                s.popleft()
            else:
                flag = False
                for i in range(len(st)):
                    if s[0] !=st[0]:
                        temp =st.popleft()
                        st.append(temp)
                    elif s[0] == st[0]:
                        flag = True
                        break
                if not flag :break
        return len(st)


