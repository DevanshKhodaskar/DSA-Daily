class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        index = -1
        summ2 = 0
        prefix = 0
        arr = []

        for i in range(len(cost)):
            arr.append(gas[i] - cost[i])

            prefix += (gas[i] - cost[i])

            if prefix < summ2:
                summ2 = prefix
                index = i

        index = (index + 1) % len(cost)

        if sum(arr) < 0:
            return -1
        else:

            ans = 0

            for i in range(index, len(cost)):
                ans += arr[i]
                if ans < 0:
                    return -1
            for j in range(0, index):
                ans += arr[j]
                if ans < 0:
                    return -1

        return index