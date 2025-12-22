class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        newPrices =  ([float("+inf")] * (n))
        newPrices[src] = 0
        tempPrices = newPrices.copy()

        for i in range(k+1):
            tempPrices = newPrices.copy()
            for s,d,c in flights:
                tempPrices[d] =min(tempPrices[d], newPrices[s]+c)

            newPrices = tempPrices
        return newPrices[dst] if newPrices[dst]<float('+inf') else -1




