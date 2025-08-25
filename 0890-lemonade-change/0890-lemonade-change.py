from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0, 20: 0}

        for i in bills:
            if i == 5:
                d[5] += 1
            elif i == 10:
                d[10] += 1
                d[5] -= 1
                
            else: 
                d[20] += 1
                if d[10] > 0:
                    d[10] -= 1
                    d[5] -= 1
                else:
                    d[5] -= 3

            print(f"d[5]: {d[5]}\td[10]: {d[10]}\td[20]: {d[20]}")
            if d[5] < 0 or d[10] < 0:
                return False

        return True