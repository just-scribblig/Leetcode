class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        n = len(piles)
        s = 0
        a = n//3

        for i in range(n-2,a-1,-2):
            s += piles[i]
        return s